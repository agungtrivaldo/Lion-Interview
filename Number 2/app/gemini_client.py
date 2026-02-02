import os
import google.generativeai as genai
import requests
from PIL import Image
from io import BytesIO

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def describe_image(image_url: str) -> str:
    img_bytes = requests.get(image_url).content
    img = Image.open(BytesIO(img_bytes))

    response = model.generate_content(
        ["Describe this image briefly.", img]
    )
    return response.text.strip()
