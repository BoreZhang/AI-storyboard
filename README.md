# AI-storyboard
# Abstract
This project aims to generate high-quality storyboards using artificial intelligence. Through comprehensive background research, selecting appropriate tools and methods, conducting experiments, and evaluating the model's performance, the report concludes with improvement suggestions.
#1. Introduction
With the rapid development of the film and animation industries, traditional storyboard creation methods are becoming insufficient for efficient production. At the same time, AI-generated content technology has shown significant improvement, with tools like Midjourney and Stable Diffusion becoming popular in the film and game industries for generating concept art. These tools have produced impressive results, replacing some of the manual work in concept design. However, in the area of storyboards, mature techniques for producing high-quality results are still limited. This project aims to explore better tools and methods for creating storyboards using AI, particularly for films. This report elaborates on the background research, methodology, experiments, results analysis, and self-evaluation.

# 2. Background Research
A storyboard is a graphic organizer consisting of illustrations or images displayed in sequence for pre-visualizing a motion picture, animation, motion graphic, or interactive media sequence. Film storyboards (sometimes referred to as shooting boards) are essentially series of frames with drawings depicting the sequence of events in a film, similar to a comic book of the film or some sections of the film produced beforehand.
AI-generated storyboards should focus on continuity in the storyline and character consistency, as they are created based on film scripts. These scripts are linked to specific actors, making character consistency crucial. The special art style of film storyboards is also a technical challenge to address.
From a technical perspective, AI-generated storyboards should primarily be based on Diffusion Models, the most important recent image generation technology. Diffusion Models provide the basic ability for image creation, especially text-to-image generation. Additionally, the research should focus on style consistency, character consistency, and storyline consistency.
Based on this foundation, we conducted research and used the following tools:
Stable Diffusion: Generates images by iteratively denoising random noise guided by the CLIP text encoder pretrained on concepts along with the attention mechanism.
Midjourney: An AI image-generation tool that creates visual art from text prompts.
DALL-E: An AI program developed by OpenAI that can create realistic images and art from natural language descriptions.
LoRA: Low-Rank Adaptation for parameter-efficient fine-tuning of models, particularly useful for adjusting styles in generated images.
ControlNet: Enhances the functionality of Stable Diffusion by introducing additional conditions during image generation.
IPAdapter: Uses images as prompts in Stable Diffusion, allowing style and composition transfer.
InstantID: Generates images preserving individual identity features without fine-tuning the model.
Story Diffusion: Utilizes Consistent Self-Attention for long-range image and video generation, ensuring content consistency across a series of generated images.

# 3. Methodology and Experiments

Project Methodology

Dataset and Preprocessing
Data Sources:
Scripts: The script of "Casablanca" as the primary textual data source.
Visual References: Film stills and actor photos from "Casablanca".
Data Cleaning:
Text Data: Ensure the script is free of errors, formatted correctly, and segmented appropriately for each scene.
Image Data: Organize and clean images, removing duplicates and ensuring high quality.
Data Annotation:
Annotate the script with scene descriptions, character actions, and dialogues.
Tag the images with relevant metadata.
Experimental Design

Experimental Objectives:
Evaluate the effectiveness of AI models in generating high-quality consistent storyboards from the "Casablanca" script.
Experimental Steps:
Script Selection: Choose script segments with two or more continuous scenes.
Baseline Comparison: Generate initial storyboards using Stable Diffusion, DALL-E, and MidJourney.
Optimization Strategies: Experiment with prompt words and plugins/tools like LoRA and InstantID.
Evaluation: Assess models based on style consistency, character consistency, story continuity, and generation speed.
Evaluation Metrics

Style Consistency: Measure the coherence of the artistic style.
Character Consistency: Evaluate the accuracy and consistency of character representations.
Story Continuity: Assess the logical flow and narrative coherence.
Generation Speed: Record the time taken to generate storyboard frames.

# 4. Specific Experiment

To test the AI models' ability to maintain story continuity and character consistency in generating storyboards, we selected script segments from "Casablanca" with clear character interactions and plot development:

Selected Script Segment

Scene One: Rick’s Café Américain

Description: Rick's bar, people drinking, dancing, and talking. Rick is observing.
Main Characters: Rick Blaine, Ilsa Lund, Sam (the pianist)
Key Plot Point: Ilsa requests Sam to play "As Time Goes By."
Dialogue: (Dialogues provided in the original report)
Scene Two: Rick and Ilsa's Reunion

Description: Rick hears the music and approaches Sam and Ilsa.
Main Characters: Rick Blaine, Ilsa Lund
Key Plot Point: Rick confronts Sam and has an emotional conversation with Ilsa.
Dialogue: (Dialogues provided in the original report)
Stress Test

Input two script segments into the AI tool without additional prompts.
Generate four images simultaneously.
Add Prompts

Add prompt words to explain characters and overall style: "create a series of continuous images, Sam portrayed by Dooley Wilson, Ilsa portrayed by Ingrid Bergman, Rick portrayed by Humphrey Bogart. The overall style should be black and white storyboard line art style."

# 5. Results Analysis and Discussion

First Test: Stable Diffusion had the worst fidelity and lowest relevance but high stylistic consistency. DALL-E produced stunning results with some stylistic consistency. Midjourney had the best effect but poor stylistic consistency.
Second Test: Stable Diffusion showed potential in character consistency. DALL-E performed the best, and Midjourney also performed well.

# 6. Conclusion
At this stage, DALL-E 3 and Midjourney are capable of creating storyboards but have issues with character consistency due to copyright constraints. Stable Diffusion, with enough plugins, can achieve similar effects, especially with Story Diffusion.

# 7. References
(Include proper citations and references for the tools and research papers mentioned, including the GitHub source and Zhou et al. 2024 paper)

Acknowledgment
Acknowledgment of the GitHub source code: https://github.com/HVision-NKU/StoryDiffusion/blob/main/Comic_Generation.ipynb
Reference: Zhou et al. 2024 StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation.
