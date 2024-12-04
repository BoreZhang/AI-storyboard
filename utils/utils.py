from email.mime import image
import torch
import base64
import gradio as gr
import numpy as np
from PIL import Image,ImageOps,ImageDraw, ImageFont
from io import BytesIO
import random

MAX_COLORS = 12

def get_random_bool():
    """
    获取一个随机布尔值
    Get a random boolean value
    """
    return random.choice([True, False])

def add_white_border(input_image, border_width=10):
    """
    为PIL图像添加指定宽度的白色边框。
    Add a white border of specified width to a PIL image.
    
    :param input_image: PIL图像对象 PIL image object
    :param border_width: 边框宽度（单位：像素） Border width (in pixels)
    :return: 带有白色边框的PIL图像对象 PIL image object with white border
    """
    border_color = 'white'  # 白色边框 White border
    # 添加边框 Add border
    img_with_border = ImageOps.expand(input_image, border=border_width, fill=border_color)
    return img_with_border

def process_mulline_text(draw, text, font, max_width):
    """
    在图像上绘制带有换行的文本。
    Draw the text on an image with word wrapping.
    
    :param draw: ImageDraw对象 ImageDraw object
    :param text: 要绘制的文本 Text to draw
    :param font: 字体 Font
    :param max_width: 文本最大宽度 Maximum width of the text
    :return: 分行后的文本列表 List of lines of text
    """
    lines = []  # 存储文本行 Store the lines of text here
    words = text.split()

    # 开始构建文本行，并在必要时换行
    # Start building lines of text, and wrap when necessary
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        # 检查添加此单词后的行宽
        # Check the width of the line with this word added
        bbox = draw.textbbox((0, 0), test_line, font=font)
        text_left, text_top, text_right, text_bottom = bbox

        width, _ = (text_right - text_left, text_bottom - text_top)

        if width <= max_width:
            # 如果适合，将此单词添加到当前行
            # If it fits, add this word to the current line
            current_line = test_line
        else:
            # 如果不适合，存储该行并开始新行
            # If not, store the line and start a new one
            lines.append(current_line)
            current_line = word
    # 添加最后一行 Add the last line
    lines.append(current_line)
    return lines 

def add_caption(image, text, position = "bottom-mid",  font = None, text_color= 'black', bg_color = (255, 255, 255) , bg_opacity = 200):
    """
    在图像上添加字幕。
    Add a caption to the image.
    
    :param image: PIL图像对象 PIL image object
    :param text: 要添加的字幕 Text to add as caption
    :param position: 字幕位置 Caption position
    :param font: 字体 Font
    :param text_color: 字幕颜色 Text color
    :param bg_color: 背景颜色 Background color
    :param bg_opacity: 背景不透明度 Background opacity
    :return: 带有字幕的PIL图像对象 PIL image object with caption
    """
    if text == "":
        return image
    image = image.convert("RGBA")
    draw = ImageDraw.Draw(image)
    width, height = image.size
    lines  =  process_mulline_text(draw,text,font,width)
    text_positions = []
    maxwidth = 0
    for ind, line in enumerate(lines[::-1]):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_left, text_top, text_right, text_bottom = bbox
        text_width, text_height = (text_right - text_left, text_bottom - text_top)
        if position == 'bottom-right':
            text_position = (width - text_width - 10, height -  (text_height + 20))
        elif position == 'bottom-left':
            text_position = (10, height -  (text_height + 20))
        elif position == 'bottom-mid':
            text_position = ((width - text_width) // 2, height -  (text_height + 20) )  # 居中文本 Center text
        height = text_position[1]
        maxwidth = max(maxwidth,text_width)
        text_positions.append(text_position)
    rectpos = (width - maxwidth) // 2
    rectangle_position = [rectpos - 5, text_positions[-1][1] - 5, rectpos + maxwidth + 5, text_positions[0][1] + text_height + 5]
    image_with_transparency = Image.new('RGBA', image.size)
    draw_with_transparency = ImageDraw.Draw(image_with_transparency)
    draw_with_transparency.rectangle(rectangle_position, fill=bg_color + (bg_opacity,))
    
    image.paste(Image.alpha_composite(image.convert('RGBA'), image_with_transparency))
    print(ind,text_position)
    draw = ImageDraw.Draw(image)
    for ind, line in enumerate(lines[::-1]):
        text_position = text_positions[ind]
        draw.text(text_position, line, fill=text_color, font=font)
    
    return image.convert('RGB')

def get_comic(images,types = "4panel",captions = [],font = None,pad_image = None):
    """
    获取漫画图像。
    Get comic images.
    
    :param images: 图像列表 List of images
    :param types: 漫画类型 Comic type
    :param captions: 字幕列表 List of captions
    :param font: 字体 Font
    :param pad_image: 填充图像 Padding image
    :return: 漫画图像列表 List of comic images
    """
    if pad_image == None:
        pad_image = Image.open("./images/pad_images.png")

    if types == "No typesetting (default)":
        return images
    elif types == "Four Pannel":
        return get_comic_4panel(images,captions,font,pad_image)
    else: # "Classic Comic Style"
        return get_comic_classical(images,captions,font,pad_image)

def get_caption_group(images_groups,captions = []):
    """
    获取字幕组。
    Get caption groups.
    
    :param images_groups: 图像组列表 List of image groups
    :param captions: 字幕列表 List of captions
    :return: 字幕组列表 List of caption groups
    """
    caption_groups = []
    for i in range(len(images_groups)):
        length = len(images_groups[i])
        caption_groups.append(captions[:length])
        captions  = captions[length:]
    if len(caption_groups[-1]) < len(images_groups[-1]):
        caption_groups[-1] = caption_groups[-1] + [""] * (len(images_groups[-1]) - len(caption_groups[-1]))
    return caption_groups

def get_comic_classical(images,captions = None,font = None,pad_image = None):
    """
    获取经典漫画图像。
    Get classical comic images.
    
    :param images: 图像列表 List of images
    :param captions: 字幕列表 List of captions
    :param font: 字体 Font
    :param pad_image: 填充图像 Padding image
    :return: 经典漫画图像列表 List of classical comic images
    """
    if pad_image == None:
        raise ValueError("pad_image is None")
    images = [add_white_border(image) for image in images]
    pad_image = pad_image.resize(images[0].size, Image.LANCZOS)
    images_groups = distribute_images2(images,pad_image)
    print(images_groups)
    if captions != None:
        captions_groups = get_caption_group(images_groups,captions)
    # print(images_groups)
    row_images = []
    for ind, img_group in enumerate(images_groups):
        row_images.append(get_row_image2(img_group ,captions= captions_groups[ind] if captions != None else None,font = font))    

    return [combine_images_vertically_with_resize(row_images)]

def get_comic_4panel(images,captions = [],font = None,pad_image = None):
    """
    获取四格漫画图像。
    Get 4-panel comic images.
    
    :param images: 图像列表 List of images
    :param captions: 字幕列表 List of captions
    :param font: 字体 Font
    :param pad_image: 填充图像 Padding image
    :return: 四格漫画图像列表 List of 4-panel comic images
    """
    if pad_image == None:
        raise ValueError("pad_image is None")
    pad_image = pad_image.resize(images[0].size, Image.LANCZOS)
    images = [add_white_border(image) for image in images]
    assert len(captions) == len(images)
    for i,caption in enumerate(captions):
        images[i] = add_caption(images[i],caption,font = font)
    images_nums = len(images)
    pad_nums = int((4 - images_nums % 4) % 4) 
    images = images + [pad_image for _ in range(pad_nums)]
    comics = []
    assert len(images)%4 == 0
    for i in range(len(images)//4):
        comics.append(combine_images_vertically_with_resize([combine_images_horizontally(images[i*4:i*4+2]), combine_images_horizontally(images[i*4+2:i*4+4])]))
    
    return comics

def get_row_image(images):
    """
    获取行图像。
    Get row images.
    
    :param images: 图像列表 List of images
    :return: 行图像 Row image
    """
    row_image_arr = []
    if len(images)>3:
        stack_img_nums = (len(images) - 2)//2
    else:
        stack_img_nums = 0
    while(len(images)>0):
        if stack_img_nums <=0:
            row_image_arr.append(images[0])
            images = images[1:]
        elif len(images)>stack_img_nums*2:
            if get_random_bool():
                row_image_arr.append(concat_images_vertically_and_scale(images[:2]))
                images = images[2:]
                stack_img_nums -=1
            else:
                row_image_arr.append(images[0])
                images = images[1:]
        else:
            row_image_arr.append(concat_images_vertically_and_scale(images[:2]))
            images = images[2:]
            stack_img_nums-=1
    return combine_images_horizontally(row_image_arr)

def get_row_image2(images,captions = None, font = None):
    """
    获取行图像（版本2）。
    Get row images (version 2).
    
    :param images: 图像列表 List of images
    :param captions: 字幕列表 List of captions
    :param font: 字体 Font
    :return: 行图像 Row image
    """
    row_image_arr = []
    if len(images)== 6:
        sequence_list = [1,1,2,2]
    elif len(images)== 4:
        sequence_list = [1,1,2]
    else:
        raise ValueError("images nums is not 4 or 6 found",len(images))
    random.shuffle(sequence_list)
    index = 0
    for length in sequence_list:
        if length == 1:
            if captions != None:
                images_tmp = add_caption(images[0],text = captions[index],font= font)
            else:
                images_tmp = images[0]
            row_image_arr.append( images_tmp)
            images = images[1:]
            index +=1
        elif length == 2:
            row_image_arr.append(concat_images_vertically_and_scale(images[:2]))
            images = images[2:]
            index +=2

    return combine_images_horizontally(row_image_arr)

def concat_images_vertically_and_scale(images,scale_factor=2):
    """
    竖直拼接图像并缩放。
    Concatenate images vertically and scale.
    
    :param images: 图像列表 List of images
    :param scale_factor: 缩放因子 Scale factor
    :return: 拼接并缩放后的图像 Concatenated and scaled image
    """
    # 加载所有图像 Load all images
    # 确保所有图像的宽度一致 Ensure all images have the same width
    widths = [img.width for img in images]
    if not all(width == widths[0] for width in widths):
        raise ValueError('All images must have the same width.')
    
    # 计算总高度 Calculate total height
    total_height = sum(img.height for img in images)
    
    # 创建新的图像，宽度与原图相同，高度为所有图像高度之和
    # Create a new image with the same width as the original and height equal to the sum of all image heights
    max_width = max(widths)
    concatenated_image = Image.new('RGB', (max_width, total_height))

    # 竖直拼接图像 Vertically concatenate images
    current_height = 0
    for img in images:
        concatenated_image.paste(img, (0, current_height))
        current_height += img.height

    # 缩放图像为1/n高度 Scale the image to 1/n height
    new_height = concatenated_image.height // scale_factor
    new_width = concatenated_image.width // scale_factor
    resized_image = concatenated_image.resize((new_width, new_height), Image.LANCZOS)
    
    return resized_image

def combine_images_horizontally(images):
    """
    横向拼接图像。
    Combine images horizontally.
    
    :param images: 图像列表 List of images
    :return: 拼接后的图像 Combined image
    """
    # 读取所有图片并存入列表 Read all images and store in a list

    # 获取每幅图像的宽度和高度 Get the width and height of each image
    widths, heights = zip(*(i.size for i in images))

    # 计算总宽度和最大高度 Calculate total width and maximum height
    total_width = sum(widths)
    max_height = max(heights)

    # 创建新的空白图片，用于拼接 Create a new blank image for combining
    new_im = Image.new('RGB', (total_width, max_height))

    # 将图片横向拼接 Horizontally combine images
    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.width

    return new_im

def combine_images_vertically_with_resize(images):
    """
    竖直拼接图像并调整大小。
    Combine images vertically and resize.
    
    :param images: 图像列表 List of images
    :return: 拼接并调整大小后的图像 Combined and resized image
    """
    # 获取所有图片的宽度和高度 Get the width and height of all images
    widths, heights = zip(*(i.size for i in images))
    
    # 确定新图片的宽度，即所有图片中最小的宽度
    # Determine the width of the new image, which is the smallest width among all images
    min_width = min(widths)
    
    # 调整图片尺寸以保持宽度一致，长宽比不变
    # Resize images to maintain consistent width, keeping aspect ratio
    resized_images = []
    for img in images:
        # 计算新高度保持图片长宽比 Calculate new height to maintain aspect ratio
        new_height = int(min_width * img.height / img.width)
        # 调整图片大小 Resize image
        resized_img = img.resize((min_width, new_height), Image.LANCZOS)
        resized_images.append(resized_img)
    
    # 计算所有调整尺寸后图片的总高度 Calculate total height of all resized images
    total_height = sum(img.height for img in resized_images)
    
    # 创建一个足够宽和高的新图片对象 Create a new image object with sufficient width and height
    new_im = Image.new('RGB', (min_width, total_height))
    
    # 竖直拼接图片 Vertically combine images
    y_offset = 0
    for im in resized_images:
        new_im.paste(im, (0, y_offset))
        y_offset += im.height

    return new_im

def distribute_images2(images, pad_image):
    """
    分配图像到组（版本2）。
    Distribute images into groups (version 2).
    
    :param images: 图像列表 List of images
    :param pad_image: 填充图像 Padding image
    :return: 图像组列表 List of image groups
    """
    groups = []
    remaining = len(images)
    if len(images) <= 8:
        group_sizes = [4]
    else:
        group_sizes = [4, 6]

    size_index = 0
    while remaining > 0:
        size = group_sizes[size_index%len(group_sizes)] 
        if remaining < size and remaining < min(group_sizes):
            size = min(group_sizes) 
        if remaining > size:
            new_group = images[-remaining: -remaining + size]
        else:
            new_group = images[-remaining:]
        groups.append(new_group)
        size_index += 1
        remaining -= size
        print(remaining,groups)
    groups[-1] = groups[-1] + [pad_image for _ in range(-remaining)]

    return groups

def distribute_images(images, group_sizes=(4, 3, 2)):
    """
    分配图像到组。
    Distribute images into groups.
    
    :param images: 图像列表 List of images
    :param group_sizes: 组大小列表 List of group sizes
    :return: 图像组列表 List of image groups
    """
    groups = []
    remaining = len(images)
    
    while remaining > 0:
        # 优先分配最大组（4张图片），再考虑3张，最后处理2张
        # Prioritize allocating the largest group (4 images), then consider 3 images, and finally handle 2 images
        for size in sorted(group_sizes, reverse=True):
            # 如果剩下的图片数量大于等于当前组大小，或者为图片总数时（也就是第一次迭代）
            # 开始创建新组
            # If the remaining number of images is greater than or equal to the current group size, or it is the total number of images (i.e., the first iteration)
            # Start creating a new group
            if remaining >= size or remaining == len(images):
                if remaining > size:
                    new_group = images[-remaining: -remaining + size]
                else:
                    new_group = images[-remaining:]
                groups.append(new_group)
                remaining -= size
                break
            # 如果剩下的图片少于最小的组大小（2张）并且已经有组了，就把剩下的图片加到最后一个组
            # If the remaining number of images is less than the minimum group size (2 images) and there are already groups, add the remaining images to the last group
            elif remaining < min(group_sizes) and groups:
                groups[-1].extend(images[-remaining:])
                remaining = 0
    
    return groups

def create_binary_matrix(img_arr, target_color):
    """
    创建二进制矩阵。
    Create a binary matrix.
    
    :param img_arr: 图像数组 Image array
    :param target_color: 目标颜色 Target color
    :return: 二进制矩阵 Binary matrix
    """
    mask = np.all(img_arr == target_color, axis=-1)
    binary_matrix = mask.astype(int)
    return binary_matrix

def preprocess_mask(mask_, h, w, device):
    """
    预处理掩码。
    Preprocess mask.
    
    :param mask_: 掩码 Mask
    :param h: 高度 Height
    :param w: 宽度 Width
    :param device: 设备 Device
    :return: 预处理后的掩码 Preprocessed mask
    """
    mask = np.array(mask_)
    mask = mask.astype(np.float32)
    mask = mask[None, None]
    mask[mask < 0.5] = 0
    mask[mask >= 0.5] = 1
    mask = torch.from_numpy(mask).to(device)
    mask = torch.nn.functional.interpolate(mask, size=(h, w), mode='nearest')
    return mask

def process_sketch(canvas_data):
    """
    处理草图。
    Process sketch.
    
    :param canvas_data: 画布数据 Canvas data
    :return: 处理后的草图数据 Processed sketch data
    """
    binary_matrixes = []
    base64_img = canvas_data['image']
    image_data = base64.b64decode(base64_img.split(',')[1])
    image = Image.open(BytesIO(image_data)).convert("RGB")
    im2arr = np.array(image)
    colors = [tuple(map(int, rgb[4:-1].split(','))) for rgb in canvas_data['colors']]
    colors_fixed = []

    r, g, b = 255, 255, 255
    binary_matrix = create_binary_matrix(im2arr, (r,g,b))
    binary_matrixes.append(binary_matrix)
    binary_matrix_ = np.repeat(np.expand_dims(binary_matrix, axis=(-1)), 3, axis=(-1))
    colored_map = binary_matrix_*(r,g,b) + (1-binary_matrix_)*(50,50,50)
    colors_fixed.append(gr.update(value=colored_map.astype(np.uint8)))

    for color in colors:
        r, g, b = color
        if any(c != 255 for c in (r, g, b)):
            binary_matrix = create_binary_matrix(im2arr, (r,g,b))
            binary_matrixes.append(binary_matrix)
            binary_matrix_ = np.repeat(np.expand_dims(binary_matrix, axis=(-1)), 3, axis=(-1))
            colored_map = binary_matrix_*(r,g,b) + (1-binary_matrix_)*(50,50,50)
            colors_fixed.append(gr.update(value=colored_map.astype(np.uint8)))

    visibilities = []
    colors = []
    for n in range(MAX_COLORS):
        visibilities.append(gr.update(visible=False))
        colors.append(gr.update())
    for n in range(len(colors_fixed)):
        visibilities[n] = gr.update(visible=True)
        colors[n] = colors_fixed[n]

    return [gr.update(visible=True), binary_matrixes, *visibilities, *colors]

def process_prompts(binary_matrixes, *seg_prompts):
    """
    处理提示。
    Process prompts.
    
    :param binary_matrixes: 二进制矩阵列表 List of binary matrices
    :param seg_prompts: 分段提示 Segment prompts
    :return: 处理后的提示数据 Processed prompt data
    """
    return [gr.update(visible=True), gr.update(value=' , '.join(seg_prompts[:len(binary_matrixes)]))]

def process_example(layout_path, all_prompts, seed_):
    """
    处理示例。
    Process example.
    
    :param layout_path: 布局路径 Layout path
    :param all_prompts: 所有提示 All prompts
    :param seed_: 随机种子 Random seed
    :return: 处理后的示例数据 Processed example data
    """
    all_prompts = all_prompts.split('***')

    binary_matrixes = []
    colors_fixed = []

    im2arr = np.array(Image.open(layout_path))[:,:,:3]
    unique, counts = np.unique(np.reshape(im2arr,(-1,3)), axis=0, return_counts=True)
    sorted_idx = np.argsort(-counts)

    binary_matrix = create_binary_matrix(im2arr, (0,0,0))
    binary_matrixes.append(binary_matrix)
    binary_matrix_ = np.repeat(np.expand_dims(binary_matrix, axis=(-1)), 3, axis=(-1))
    colored_map = binary_matrix_*(255,255,255) + (1-binary_matrix_)*(50,50,50)
    colors_fixed.append(gr.update(value=colored_map.astype(np.uint8)))

    for i in range(len(all_prompts)-1):
        r, g, b = unique[sorted_idx[i]]
        if any(c != 255 for c in (r, g, b)) and any(c != 0 for c in (r, g, b)):
            binary_matrix = create_binary_matrix(im2arr, (r,g,b))
            binary_matrixes.append(binary_matrix)
            binary_matrix_ = np.repeat(np.expand_dims(binary_matrix, axis=(-1)), 3, axis=(-1))
            colored_map = binary_matrix_*(r,g,b) + (1-binary_matrix_)*(50,50,50)
            colors_fixed.append(gr.update(value=colored_map.astype(np.uint8)))

    visibilities = []
    colors = []
    prompts = []
    for n in range(MAX_COLORS):
        visibilities.append(gr.update(visible=False))
        colors.append(gr.update())
        prompts.append(gr.update())

    for n in range(len(colors_fixed)):
        visibilities[n] = gr.update(visible=True)
        colors[n] = colors_fixed[n]
        prompts[n] = all_prompts[n+1]

    return [gr.update(visible=True), binary_matrixes, *visibilities, *colors, *prompts,
            gr.update(visible=True), gr.update(value=all_prompts[0]), int(seed_)]    