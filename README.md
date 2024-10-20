
# Streamlit app for Flux with togather AI

This Streamlit app leverages the Together AI API to generate images using the FLUX.1-schnell model. It allows users to enter prompts, select the number of images and steps, and generate high-quality images based on their descriptions.


![Alt text](path/to/image)

## Features

- **Enter your own prompt**: Describe the image you want the model to generate.
- **Choose the number of images**: Specify how many images you want to generate.
- **Control the number of steps**: Choose how detailed and accurate the generation process will be.
- **Generated images preview**: See all generated images and download the one you like.

## Prerequisites

To run this app, you need:

- Python 3.10
- Streamlit installed (`pip install streamlit`)
- Together AI API key

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/streamlit-image-generator.git
   ```
2. Navigate into the project directory:
   ```bash
   cd streamlit-image-generator
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Obtain an API key from [Together AI](https://together.ai) and enter it in the app's settings.

## How to Run

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Enter a prompt, select the number of images and steps, then hit **Generate** to create the images.

4. You will see the generated images on the right-hand side. You can click **Download Image** to save your preferred image.

## Example

Below is a screenshot of the app in action, generating an image of a woman in a backless dress at the Cannes Film Festival.

![App Screenshot](./image.png)

Enjoy generating beautiful AI images with just a few clicks!
