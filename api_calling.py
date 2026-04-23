from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

# pil_image = Image.open("path_to_your_image.jpg")


def generate_response(image):
    prompt = """Debug the code in the image and provide insights and potential solutions. Focus on identifying the error message, the line of code causing the issue, and suggest possible fixes or improvements."""
    contents = [image, prompt]

    response = client.models.generate_content(
            model = "gemini-3-flash-preview",
            contents = contents
    )
    return response.text

