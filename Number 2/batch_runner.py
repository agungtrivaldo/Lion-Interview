import os
import csv
import requests

API_URL = "http://localhost:8000/analyze-image"
IMAGE_FOLDER = "./images/"
OUTPUT_CSV = "summary.csv"

def run_batch():
    rows = []

    for file in os.listdir(IMAGE_FOLDER):
        if not file.lower().endswith((".jpg", ".png", ".jpeg")):
            continue

        image_url = f"http://localhost:8000/images/{file}"

        response = requests.post(
            API_URL,
            json={"image_url": image_url},
            timeout=30
        )

        print(file, response.status_code)

        if not response.text.strip():
            raise ValueError("Empty response from API")

        resp = response.json()

        rows.append({
            "image_name": file,
            "result": resp.get("result", "")
        })

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["image_name", "result"])
        writer.writeheader()
        writer.writerows(rows)

    print("CSV generated:", OUTPUT_CSV)

if __name__ == "__main__":
    run_batch()
