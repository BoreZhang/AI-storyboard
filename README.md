# AI-Generated Storyboard

## Abstract
This project aims to generate high-quality storyboards using artificial intelligence, with a focus on adapting and extending existing technologies. Through comprehensive background research, selecting appropriate tools and methods, conducting experiments, and evaluating model performance, we present our findings and suggestions for improvement in the field of AI-generated storyboards.

## 1. Introduction
The rapid development of the film and animation industries has created a need for more efficient storyboard creation methods. Artificial Intelligence (AI) tools like Midjourney and Stable Diffusion have shown promising results in generating concept art for films and games [Rombach, R., et al. (2022)][Croitoru, F. A., et al. (2023)]. However, the application of these technologies to storyboard creation is still in its early stages.

This project aims to explore and adapt existing AI tools and methods to create high-quality storyboards, with a particular focus on film storyboards. We will examine the challenges of maintaining character consistency, style continuity, and narrative coherence across multiple scenes.

## 2. Background Research
A storyboard is a sequence of illustrations or images used to pre-visualize a motion picture, animation, or interactive media sequence [Hart, J. (2008)]. Film storyboards, in particular, require consistent character representation, adherence to script details, and a specific artistic style.

Our research focuses on AI-generated content, primarily using Diffusion Models, which have shown significant potential in image generation tasks [Dhariwal, P., & Nichol, A. (2021)]. We examined several key technologies and tools:

- **Stable Diffusion** [Rombach, R., et al. (2022)]: Generates images by iteratively denoising random noise until a configured number of steps have been reached, guided by the CLIP text encoder pretrained on concepts along with the attention mechanism, resulting in the desired image depicting a representation of the trained concept.
  
- **Midjourney** [Midjourney, Inc. (2022)]: An AI image-generation tool that creates visual art from text prompts, similar to platforms like DALL-E and Stable Diffusion.
  
- **DALL-E** [Ramesh, A., et al. (2022)]: An AI program that creates realistic images and art from descriptions in natural language, combining concepts, attributes, and styles to generate original, realistic images.
  
- **LoRA (Low-Rank Adaptation)** [Hu, E. J., et al. (2021)]: A method of Parameter-Efficient Fine-Tuning (PEFT) used to adjust the style of generated images by fine-tuning a small number of parameters while keeping the original model structure unchanged.
  
- **ControlNet** [Zhang, L., et al. (2023)]: A neural network that fine-tunes the image generation process by introducing additional conditions, enhancing the functionality of Stable Diffusion.
  
- **IPAdapter** [Ye, H., et al. (2023)]: Enables users to copy the style, composition, or facial features from a reference image to guide the image generation process.
  
- **InstantID** [Wang, Q., et al. (2024)]: A method of Zero-Shot Identity-Preserving Generation that can generate images that preserve individual identity features in seconds without fine-tuning the model.

## 3. Methodology
In this study, we primarily focus on addressing the challenge of character continuity in AI-generated storyboards. We explored several common solutions and concentrated on two innovative approaches: StoryDiffusion and AutoStudio.

### 1. Common Solutions:
- Using consistent character description prompts
- Employing fine-tuning techniques like LoRA to enhance specific character representations
- Utilizing tools like ControlNet to maintain pose and style consistency

### 2. StoryDiffusion [Zhou, Y., et al. (2024)]:
An innovative technology based on diffusion models, designed specifically for long-range image and video generation. It calculates self-attention in a new way called Consistent Self-Attention, significantly boosting consistency between generated images.

### 3. AutoStudio [Zhang, T., Wu, Y., Li, X., Ma, Y., & Zhang, Y. (2024)]:
An innovative large-scale language model (LLM) technology specifically designed for automated storyboard and comic generation. It integrates text understanding, scene layout, and image generation capabilities, enhancing consistency and expressiveness of characters.

Our experiments show that while StoryDiffusion performs better in overall generation quality, it exhibits some decline in character consistency when dealing with multi-character scenes. To address this issue, we incorporated the AutoStudio method, leveraging its multi-agent system to enhance character consistency and scene coherence.

By combining these two approaches, we aim to develop an AI storyboard generation system that maintains overall narrative coherence while ensuring individual character consistency.

## 4. Experiments
To test the AI models' ability to maintain story continuity and character consistency in generating storyboards, we selected a script segment from "Casablanca" that includes two or more continuous scenes.

### Selected Script Segment:
- **Scene One: Rick’s Café Américain**
  - *Description:* Rick's bar, where people are drinking, dancing, and talking. Rick is sitting in a corner, observing the entire room.
  - *Main Characters:* Rick Blaine, Ilsa Lund, Sam (the pianist)
  - *Key Plot Point:* Ilsa talks to Sam and requests him to play "As Time Goes By."
  
- **Scene Two: Rick and Ilsa's Reunion**
  - *Description:* Rick hears the music and approaches Sam and Ilsa. Rick and Ilsa meet, filled with emotional tension.
  - *Main Characters:* Rick Blaine, Ilsa Lund
  - *Key Plot Point:* Rick confronts Sam about playing the song and has an intense emotional conversation with Ilsa.

### Testing Steps:
1. **Stress Test:** Input the script segments directly into the AI tool without adding additional prompt words. All tools generated four images simultaneously.
  
2. **Optimized Generation:** Added prompt words to explain the actors corresponding to the characters and the overall style of the scene, such as “Create a series of continuous images, Sam portrayed by Dooley Wilson, Ilsa portrayed by Ingrid Bergman, Rick portrayed by Humphrey Bogart. The overall style should be black and white storyboard, line art style.”

## 5. Results Analysis and Discussion
In the stress test, Stable Diffusion showed poor fidelity and plot relevance but maintained stylistic consistency. DALL-E 3 produced high-quality results with good stylistic consistency. Midjourney had the best visual quality but poor stylistic consistency.

In the optimized generation, Stable Diffusion improved in character consistency but still performed worst overall. DALL-E performed best, with Midjourney also showing good results.

### StoryDiffusion Performance:
StoryDiffusion demonstrates commendable character consistency; however, when more than two characters are present in a scene, this consistency tends to decline, resulting in discrepancies between adjacent images.

### AutoStudio Performance:
AutoStudio offers four specially designed agents that interact with users in real-time, integrating any necessary content, LLM architectures, and diffusion backbones into the framework. Although the overall image generation quality of AutoStudio is not as high as StoryDiffusion, it excels in supporting consistency across multiple characters.

I attempted to incorporate some of the concepts from AutoStudio into the StoryDiffusion project to enhance character consistency when multiple characters appear. While I observed some improvement, my limited mathematical background and incomplete understanding of AutoStudio's underlying principles prevented me from fully replicating its approach. Nevertheless, the preliminary results are promising, but there's much more to be done. I plan to further explore and refine this area in the future.

## 6. Conclusion
Our experiments show that while DALL-E 3 and Midjourney are approaching the capability to create usable storyboards, they still struggle with maintaining character consistency due to copyright issues. Stable Diffusion, when augmented with appropriate plugins, shows potential for improvement.

The recently released StoryDiffusion [Zhou, Y., et al. (2024)] and AutoStudio [Zhang, T., Wu, Y., Li, X., Ma, Y., & Zhang, Y. (2024)] offer promising capabilities for maintaining consistency across multiple images, which is crucial for storyboard generation. Our future work will focus on adapting and extending this technology for film storyboard creation.

## 7. References
1. Rombach, R., et al. (2022). High-resolution image synthesis with latent diffusion models. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 10684-10695.
2. Croitoru, F. A., et al. (2023). Diffusion models in vision: A survey. IEEE Transactions on Pattern Analysis and Machine Intelligence.
3. Hart, J. (2008). The Art of the Storyboard: A filmmaker's introduction. Focal Press.
4. Dhariwal, P., & Nichol, A. (2021). Diffusion models beat GANs on image synthesis. Advances in Neural Information Processing Systems, 34, 8780-8794.
5. Rombach, R., et al. (2022). High-resolution image synthesis with latent diffusion models. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 10684-10695.
6. Midjourney, Inc. (2022). Midjourney: AI-powered creative tool. https://www.midjourney.com/
7. Ramesh, A., et al. (2022). Hierarchical text-conditional image generation with CLIP latents. arXiv preprint arXiv:2204.06125.
8. Hu, E. J., et al. (2021). LoRA: Low-rank adaptation of large language models. arXiv preprint arXiv:2106.09685.
9. Zhang, L., et al. (2023). Adding conditional control to text-to-image diffusion models. Proceedings of the IEEE/CVF International Conference on Computer Vision.
10. Ye, H., et al. (2023). IP-adapter: Text compatible image prompt adapter for text-to-image diffusion models. arXiv preprint arXiv:2308.06721.
11. Wang, Q., et al. (2024). InstantID: Zero-shot identity-preserving generation in seconds. arXiv preprint arXiv:2401.07519.
12. Zhou, Y., et al. (2024). StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation. arXiv preprint arXiv:2405.01434.
13. Zhang, T., Wu, Y., Li, X., Ma, Y., & Zhang, Y. (2024). An Efficient Transformer with Multi-modal Interaction for Image and Text Matching. arXiv preprint arXiv:2406.01388. Available at: https://arxiv.org/abs/2406.01388 (Accessed: 27 August 2024).
