# AI Storyboard Generation with StoryDiffusion

## Project Overview

This project is an AI-driven storyboard generation tool developed based on the StoryDiffusion framework. It integrates features from AutoStudio and introduces new modules aimed at enhancing character consistency, especially in scenes involving multiple characters. This enhancement makes the storyboard generation process more reliable and visually coherent, ensuring that characters maintain their identity and visual traits across different storyboard frames. 
Video Explanation on https://1drv.ms/v/s!As7RbNhdzSP2gvQ9WQyjq5xm9YL8-g?e=F5rR0O

## Features

- **Character Consistency:** Enhanced modules ensure characters retain consistent visual traits, even in multi-character scenes.
- **Integrated Diffusion Models:** Supports multiple Stable Diffusion models, including `Juggernaut`, `RealVision`, and `SDXL`.
- **Customizable Styles:** Apply various styles to tailor the aesthetic of the generated storyboards.
- **Interactive Interface:** Utilizes Gradio for a user-friendly, interactive experience.

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.8+
- NumPy
- Torch
- Gradio
- Pillow
- Diffusers

You can install the required packages using:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

> Note: The \`torch._custom_ops\` module needs to be available in your environment. Ensure you have the correct version of PyTorch installed.

## Usage

1. Clone the repository and navigate to the project directory.
2. Run the Jupyter notebook \`Storyboard_Generation.ipynb\` to start generating storyboards.
3. Modify the configuration settings to customize your storyboard generation, including style, model selection, and additional parameters.

## Configuration

The project supports various configuration settings to tailor the storyboard generation process:

- **Models:** Choose from multiple diffusion models for different stylistic outputs.
- **Styles:** Apply predefined or custom styles to the generated images.
- **Seed:** Control randomness in generation using a fixed seed.

## Troubleshooting

If you encounter issues, ensure all dependencies are correctly installed and that your environment meets the project requirements. For specific errors related to Torch, consider checking your PyTorch installation.


## Acknowledgments

This project builds upon the work of others in the community. Special thanks to the following projects:

- [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) for providing the foundational framework for this project.
- [AutoStudio](https://github.com/donahowe/AutoStudio) for inspiring the enhanced character consistency features.
"""

