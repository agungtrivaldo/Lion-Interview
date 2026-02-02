from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from schemas import ImageRequest
from blur import is_blur
from gemini_client import describe_image

app = FastAPI()

# 🔥 INI PENTING
app.mount("/images", StaticFiles(directory="images"), name="images")


@app.post("/analyze-image")
def analyze_image(payload: ImageRequest):
    if is_blur(payload.image_url):
        return {"result": "blur"}

    description = describe_image(payload.image_url)
    return {"result": description}
