import requests
import numpy as np
import cv2
from fastapi import HTTPException


def download_image(url: str):
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to download image")

    image_array = np.frombuffer(response.content, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if image is None:
        raise HTTPException(status_code=400, detail="Invalid image")

    return image
