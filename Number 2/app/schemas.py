from pydantic import BaseModel

class ImageRequest(BaseModel):
    image_url: str

class ImageResponse(BaseModel):
    result: str
