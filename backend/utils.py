import base64, os
from PIL import Image
import io

def image_path_to_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def base64_to_image(b64: str, save_path: str):
    img_data = base64.b64decode(b64)
    with open(save_path, "wb") as f:
        f.write(img_data)

def compress_image_base64(b64: str, quality: int = 60) -> str:
    """Compress image to reduce API payload size — faster response"""
    img_data = base64.b64decode(b64)
    img = Image.open(io.BytesIO(img_data))
    img = img.resize((640, 480))  # Resize to standard
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=quality)
    return base64.b64encode(buffer.getvalue()).decode()