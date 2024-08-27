Project Report of AI-Generated Storyboard

Abstract
This project aims to generate high-quality storyboards using artificial intelligence, with a focus on adapting and extending existing technologies. Through comprehensive background research, selecting appropriate tools and methods, conducting experiments, and evaluating model performance, we present our findings and suggestions for improvement in the field of AI-generated storyboards.
1. Introduction
The rapid development of the film and animation industries has created a need for more efficient storyboard creation methods. Artificial Intelligence (AI) tools like Midjourney and Stable Diffusion have shown promising results in generating concept art for films and games [Rombach, R., et al. (2022)..][Croitoru, F. A., et al. (2023) ]. However, the application of these technologies to storyboard creation is still in its early stages.
This project aims to explore and adapt existing AI tools and methods to create high-quality storyboards, with a particular focus on film storyboards. We will examine the challenges of maintaining character consistency, style continuity, and narrative coherence across multiple scenes.

2. Background Research
A storyboard is a sequence of illustrations or images used to pre-visualize a motion picture, animation, or interactive media sequence [Hart, J. (2008) ]. Film storyboards, in particular, require consistent character representation, adherence to script details, and a specific artistic style.
Our research focuses on AI-generated content, primarily using Diffusion Models, which have shown significant potential in image generation tasks [Dhariwal, P., & Nichol, A. (2021)]. We examined several key technologies and tools:
•	Stable Diffusion [Rombach, R., et al. (2022).]
•	Midjourney [Midjourney, Inc. (2022)]
•	DALL-E [Ramesh, A., et al. (2022) ]
•	LoRA (Low-Rank Adaptation) [Hu, E. J., et al. (2021) ]
•	ControlNet [Zhang, L., et al. (2023) ]
•	IPAdapter [Ye, H., et al. (2023) ]
•	InstantID [Wang, Q., et al. (2024) ]
Stable Diffusion[Rombach, R., et al. (2022).]: The Stable Diffusion model generates images by iteratively denoising random noise until a configured number of steps have been reached, guided by the CLIP text encoder pretrained on concepts along with the attention mechanism, resulting in the desired image depicting a representation of the trained concept.  
The principle of Stable Diffusion technology is based on two main steps: Forward Diffusion and Reverse Diffusion.
1. Forward Diffusion: During this phase, an original piece of data (like an image) is subjected to a process where calculated random noise is incrementally added. Repeating this step gradually degrades the quality of the data, moving it from its initial state towards a state of randomness.
2. Reverse Diffusion: This phase is the reverse operation of Forward Diffusion. The goal is to methodically remove the noise that was added, step by step reconstructing the process from the noisy state back to the original data.

Midjourney[Midjourney, Inc. (2022)]: Midjourney is an AI image-generation tool that creates visual art from text prompts. The software was developed by Midjourney, Inc., a San Francisco research lab founded by David Holz of Leap Motion.
Functioning similarly to renowned platforms like OpenAI's DALL-E and Stable Diffusion, Midjourney crafts visuals from textual descriptions, commonly termed as "prompts". Having launched its open beta phase on July 12, 2022, this innovative tool is becoming increasingly popular.

DALL-E[Ramesh, A., et al. (2022) ]: DALL-E is an AI program developed by OpenAI that can create realistic images and art from a description in natural language. DALL-E combines concepts, attributes, and styles to create original, realistic images. For instance, it can generate images based on the description "a bowl of soup that is a portal to another dimension" and can also make realistic edits to existing images, considering factors like shadows, reflections, and textures.
In terms of technical principles, DALL-E first inputs a text prompt into a text encoder, which is trained to map the prompt to a representation space. Next, a model called the prior maps the text encoding to a corresponding image encoding that captures the semantic information contained in the text encoding. Finally, an image decoder stochastically generates an image that is a visual manifestation of this semantic information.

LoRA[Hu, E. J., et al. (2021) ]:Based on Stable Diffusion, LoRA standing for Low-Rank Adaptation, is a method of Parameter-Efficient Fine-Tuning (PEFT). It introduces low-rank matrices into specific layers of the model and fine-tunes only these matrix parameters, thus adjusting the model's performance or output without significantly increasing the computational load.
The core advantage of LoRA lies in its ability to rapidly adapt and customize the model by fine-tuning a small number of parameters while keeping the original model structure unchanged. For instance, in Stable Diffusion, LoRA can be used to adjust the style of generated images, such as anime, ink painting, or pixel style, or to edit and repair specific images.
In terms of technical principles, LoRA inserts a new weight matrix ( \Delta W ) next to the model's weight matrix ( W ), and further decomposes ( \Delta W ) into the product of two low-rank matrices ( A ) and ( B ), that is, ( \Delta W = BA ), where ( r ) is much smaller than ( d ) and ( k ), achieving dimensionality reduction and fine-tuning of the original model.

ControlNet [Zhang, L., et al. (2023) ]: ControlNet is an innovative neural network that fine-tunes the image generation process of Stable Diffusion models by introducing additional conditions. ControlNet was first proposed by Lvmin Zhang and his team in their research paper "Adding Conditional Control to Text-to-Image Diffusion Models," which not only enhances the functionality of Stable Diffusion but also achieves a qualitative leap in the precision and diversity of image generation.
In terms of technical principles, the working principle of ControlNet lies in its attachment of trainable network modules to different parts of the U-Net (noise predictor) of the Stable Diffusion model. During training, ControlNet receives text prompts and control maps as inputs, learning how to generate images based on these conditions.

IPAdapter[Ye, H., et al. (2023) ]: The IPAdapter technology based on Stable Diffusion, also known as Image Prompt Adapter, is an extension for using images as prompts in Stable Diffusion. It enables users to copy the style, composition, or facial features from a reference image to guide the image generation process.
In terms of technical principles, the IPAdapter trains separate cross-attention layers for image features, making it more effective in steering the image generation process. For instance, it can blend attributes from both an image prompt and a text prompt to create a new, modified image. This new image is then merged with the input image, which has been pre-processed using ControlNet, thus achieving style and composition transfer.

InstantID[Wang, Q., et al. (2024) ]: InstantID is a method of Zero-Shot Identity-Preserving Generation. It can generate images that preserve individual identity features in seconds without the need for fine-tuning the model. The main function of InstantID is to quickly generate personalized images with high fidelity using a single reference image.
In terms of technical principles, InstantID is built on top of the Stable Diffusion model, utilizing an efficient diffusion process in a low-dimensional latent space instead of pixel space for image generation. This approach not only saves computational resources but also allows for the rapid generation of consistent personalized images without sacrificing image quality.

3. Methodology
In this study, we primarily focus on addressing the challenge of character continuity in AI-generated storyboards. We explored several common solutions and concentrated on two innovative approaches: StoryDiffusion and AutoStudio.
1.	Common Solutions: 
o	Using consistent character description prompts
o	Employing fine-tuning techniques like LoRA to enhance specific character representations
o	Utilizing tools like ControlNet to maintain pose and style consistency
2.	Story Diffusion[Zhou, Y., et al. (2024) ]: Story Diffusion is an innovative technology based on diffusion models, designed specifically for long-range image and video generation. It calculates self-attention in a new way called Consistent Self-Attention, which significantly boosts the consistency between generated images and augments existing diffusion-based text-to-image models in a zero-shot manner.
In terms of technical principles, Story Diffusion proposes a new way of self-attention calculation, termed Consistent Self-Attention, that maintains content consistency across a series of generated images, especially those containing subjects and complex details. Moreover, to extend the method to long-range video generation, the researchers introduced a novel semantic space temporal motion prediction module, named Semantic Motion Predictor. It is trained to estimate the motion conditions between two provided images in semantic spaces. This module converts the generated sequence of images into videos with smooth transitions and consistent subjects that are significantly more stable than modules based only on latent spaces, especially in the context of long video generation.
3.	AutoStudio [Zhang, T., Wu, Y., Li, X., Ma, Y., & Zhang, Y. (2024) ]: AutoStudio is an innovative large-scale language model (LLM) technology specifically designed for automated storyboard and comic generation. It significantly improves the efficiency and quality of visual narrative creation by integrating text understanding, scene layout and image generation capabilities. In terms of technical principles, AutoStudio proposes a new scene layout generation method called Contextual Layout Generation. This method can automatically generate a scene layout that conforms to narrative logic based on the storyline and character descriptions. In addition, in order to enhance the consistency and expressiveness of characters, the researchers introduced a novel character embedding module named Character Embedding Module. The module is trained to extract features from a small number of character images and maintain character visual consistency throughout the story generation process. In order to extend this method to the generation of long-form comics and animation storyboards, AutoStudio also introduces an innovative narrative coherence prediction module called Narrative Coherence Predictor. It predicts and generates coherent transition scenes by analyzing the semantic relationships between previous and subsequent scenes, thereby significantly improving the fluency and coherence of long visual narratives. This module can produce more stable and coherent results when generating long-form comic and animation storyboards than methods based only on a single scene, especially when dealing with complex plot development and character interactions.

Our experiments show that while StoryDiffusion performs better in overall generation quality, it exhibits some decline in character consistency when dealing with multi-character scenes. To address this issue, we incorporated the AutoStudio method, leveraging its multi-agent system to enhance character consistency and scene coherence.
By combining these two approaches, we aim to develop an AI storyboard generation system that maintains overall narrative coherence while ensuring individual character consistency.

4. Experiments
To test the AI models' ability to maintain story continuity and character consistency in generating storyboards, we need to select a script segment from "Casablanca" that includes two or more continuous scenes. Below is a suitable segment from "Casablanca" that meets these criteria, containing two continuous scenes with clear character interactions and plot development:
Selected Script Segment
Scene One: Rick’s Café Américain
•	Description: Rick's bar, people are drinking, dancing, and talking. Rick is sitting in a corner, observing the entire room.
•	Main Characters: Rick Blaine, Ilsa Lund, Sam (the pianist)
•	Key Plot Point: Ilsa talks to Sam and requests him to play "As Time Goes By."
Dialogue:
Ilsa: Play it once, Sam. For old times' sake. Sam: I don’t know what you mean, Miss Ilsa. Ilsa: Play it, Sam. Play "As Time Goes By." Sam: Oh, I can’t remember it, Miss Ilsa. I’m a little rusty on it. Ilsa: I’ll hum it for you. (She begins to hum, Sam joins in on the piano) 
Scene Two: Rick and Ilsa's Reunion
•	Description: Rick hears the music and approaches Sam and Ilsa. Rick and Ilsa meet, filled with emotional tension.
•	Main Characters: Rick Blaine, Ilsa Lund
•	Key Plot Point: Rick confronts Sam about playing the song and has an intense emotional conversation with Ilsa.
Dialogue:
Rick: (to Sam) I thought I told you never to play that song! 
Ilsa: Hello, Rick. 
Rick: Hello, Ilsa. 
Ilsa: I didn't expect to see you here. 
Rick: It's been a long time. 
Ilsa: Yes, it's been a long time. 

1. For a stress test
Input two script segments directly into the AI tool for testing without adding any additional prompt words. Stable Diffusion will not use any plugins or LoRA. All tools will generate four images simultaneously.  
 
Storydiffusion 

2. Add prompt
Add some prompt words to explain the actors corresponding to the characters and the overall style of the scene. The promts are “create a series of continuous images , Sam portrayed by Dooley Wilson and Ilsa portrayed by Ingrid Bergman,Rick portrayed by Humphrey Bogart .The overall style should be black and white storyboard, line art style.”  
Add some prompt words to explain the actors corresponding to the characters and the overall style of the scene. The promts are “create a series of continuous images , Sam portrayed by Dooley Wilson and Ilsa portrayed by Ingrid Bergman,Rick portrayed by Humphrey Bogart .The overall style should be black and white storyboard, line art style.”
   


5. Results Analysis and Discussion
In the stress test, Stable Diffusion showed poor fidelity and plot relevance but maintained stylistic consistency. DALL-E 3 produced high-quality results with good stylistic consistency. Midjourney had the best visual quality but poor stylistic consistency.
In the optimized generation, Stable Diffusion improved in character consistency but still performed worst overall. DALL-E performed best, with Midjourney also showing good results.
StoryDiffusion demonstrates commendable character consistency; however, when more than two characters are present in a scene, this consistency tends to decline, resulting in discrepancies between adjacent images. On the other hand, AutoStudio offers four specially designed agents that interact with users in real-time, integrating any necessary content, LLM architectures, and diffusion backbones into the framework. Although the overall image generation quality of AutoStudio is not as high as StoryDiffusion, it excels in supporting consistency across multiple characters.
I attempted to incorporate some of the concepts from AutoStudio into the StoryDiffusion project to enhance character consistency when multiple characters appear. While I observed some improvement, my limited mathematical background and incomplete understanding of AutoStudio's underlying principles prevented me from fully replicating its approach. Nevertheless, the preliminary results are promising, but there's much more to be done. I plan to further explore and refine this area in the future.


6. Conclusion
Our experiments show that while DALL-E 3 and Midjourney are approaching the capability to create usable storyboards, they still struggle with maintaining character consistency due to copyright issues. Stable Diffusion, when augmented with appropriate plugins, shows potential for improvement.
The recently released StoryDiffusion [Zhou, Y., et al. (2024)]and AutoStudio[Zhang, T., Wu, Y., Li, X., Ma, Y., & Zhang, Y. (2024) ] offers promising capabilities for maintaining consistency across multiple images, which is crucial for storyboard generation. Our future work will focus on adapting and extending this technology for film storyboard creation.


7. References
1.	Rombach, R., et al. (2022). High-resolution image synthesis with latent diffusion models. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 10684-10695.
2.	Croitoru, F. A., et al. (2023). Diffusion models in vision: A survey. IEEE Transactions on Pattern Analysis and Machine Intelligence.
3.	Hart, J. (2008). The Art of the Storyboard: A filmmaker's introduction. Focal Press.
4.	Dhariwal, P., & Nichol, A. (2021). Diffusion models beat GANs on image synthesis. Advances in Neural Information Processing Systems, 34, 8780-8794.
5.	Rombach, R., et al. (2022). High-resolution image synthesis with latent diffusion models. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 10684-10695.
6.	Midjourney, Inc. (2022). Midjourney: AI-powered creative tool. https://www.midjourney.com/
7.	Ramesh, A., et al. (2022). Hierarchical text-conditional image generation with CLIP latents. arXiv preprint arXiv:2204.06125.
8.	Hu, E. J., et al. (2021). LoRA: Low-rank adaptation of large language models. arXiv preprint arXiv:2106.09685.
9.	Zhang, L., et al. (2023). Adding conditional control to text-to-image diffusion models. Proceedings of the IEEE/CVF International Conference on Computer Vision.
10.	Ye, H., et al. (2023). IP-adapter: Text compatible image prompt adapter for text-to-image diffusion models. arXiv preprint arXiv:2308.06721.
11.	Wang, Q., et al. (2024). InstantID: Zero-shot identity-preserving generation in seconds. arXiv preprint arXiv:2401.07519.
12.	Zhou, Y., et al. (2024). StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation. arXiv preprint arXiv:2405.01434.
13.	Zhang, T., Wu, Y., Li, X., Ma, Y., & Zhang, Y. (2024) 'An Efficient Transformer with Multi-modal Interaction for Image and Text Matching', arXiv preprint arXiv:2406.01388. Available at: https://arxiv.org/abs/2406.01388 (Accessed: 27 August 2024).

