import cv2
import numpy as np
import requests


def is_blur(image_url: str, threshold: float = 100.0) -> bool:
    response = requests.get(image_url)

    if response.status_code != 200:
        raise ValueError(f"Image not accessible: {image_url}")

    image_array = np.frombuffer(response.content, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)

    # 🔥 SAFETY CHECK
    if image is None:
        raise ValueError("Failed to decode image")

    variance = cv2.Laplacian(image, cv2.CV_64F).var()
    return variance < threshold
