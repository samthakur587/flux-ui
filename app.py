import streamlit as st
import requests
from together import Together
from PIL import Image
from io import BytesIO
import os
import base64

def setup_together_client():
    try:
        together = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
        return together
    except Exception as e:
        st.error(f"Error setting up client: {str(e)}")
        return None

def map_model_name(model):
    model_map = {
        "FLUX.1-pro": "black-forest-labs/FLUX.1-pro",
        "FLUX.1-schnell": "black-forest-labs/FLUX.1-schnell",
        "FLUX1.1-pro": "black-forest-labs/FLUX.1.1-pro",
    }
    return model_map.get(model, model)

def get_image_download_link(img_content, filename):
    """Generates a link to download the image"""
    b64 = base64.b64encode(img_content).decode()
    return f'<a href="data:image/png;base64,{b64}" download="{filename}"><button style="padding: 5px 10px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; margin: 5px 0;">Download Image</button></a>'

def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content)), response.content
    except Exception as e:
        st.error(f"Error downloading image: {str(e)}")
        return None, None

def generate_images(together_client, prompt, model,num_steps=10, num_images=4):
    try:
        response = together_client.images.generate(
            prompt=prompt,
            model=map_model_name(model),
            steps=num_steps,
            n=num_images,
        )
        
        # Extract image URLs from response
        images = []
        image_contents = []
        for image_data in response.data:
            if image_data.url:
                img, img_content = download_image(image_data.url)
                if img and img_content:
                    images.append(img)
                    image_contents.append(img_content)
        return images, image_contents
    except Exception as e:
        st.error(f"Error generating images: {str(e)}")
        return [], []
    

def main():
    st.set_page_config(layout="wide", page_title="Together AI Image Generator")
    
    # Sidebar for API Key
    with st.sidebar:
        st.title("Settings")
        api_key = st.text_input("Enter Together AI API Key", type="password")
        os.environ["TOGETHER_API_KEY"] = api_key
        # Model selection dropdown
        model = st.selectbox(
            "Choose your favorite model",
            ["FLUX.1-pro", "FLUX.1-schnell", "FLUX1.1-pro"],  # Reordered to put default first
            index=1,  # Set default to first option (FLUX.1-pro)
            help="Select the AI model for image generation"
        )
        
    # Create two columns for the main content
    left_col, right_col = st.columns([1, 1])
    
    # Left column content
    with left_col:
        st.title("Image Generator")
        prompt = st.text_area("Enter your prompt", height=100)
        num_images = st.slider("Number of images", min_value=1, max_value=10, value=4)
        num_steps = st.slider("Number of steps", min_value=1, max_value=20, value=10)
        generate_button = st.button("Generate")
        
    # Right column content
    with right_col:
        st.title("Generated Images")
        if generate_button and prompt and api_key:
            with st.spinner("Generating images..."):
                # Setup Together client
                together_client = setup_together_client()
                if together_client:
                    # Generate images using selected model
                    images, image_contents = generate_images(together_client, prompt, model,num_steps, num_images)
                    if images:
                        # Create a grid of images with download buttons
                        cols = st.columns(2)  # 2x2 grid
                        for idx, (img, img_content) in enumerate(zip(images, image_contents)):
                            with cols[idx % 2]:
                                # Display image
                                st.image(img, caption=f"Generated Image {idx+1}", use_column_width=True)
                                # Display download button
                                st.markdown(
                                    get_image_download_link(img_content, f"generated_image_{idx+1}.png"), 
                                    unsafe_allow_html=True
                                )
        else:
            st.info("Enter a prompt and API key, then click Generate to create images")

if __name__ == "__main__":
    main()