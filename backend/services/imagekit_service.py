
from imagekitio import ImageKit



from config import IMAGEKIT_PRIVATE_KEY, IMAGEKIT_PUBLIC_KEY, IMAGEKIT_URL_ENDPOINT
imagekit = ImageKit(
    private_key=IMAGEKIT_PRIVATE_KEY,
    public_key=IMAGEKIT_PUBLIC_KEY,
    url_endpoint=IMAGEKIT_URL_ENDPOINT,
)

def upload_image(file_bytes: bytes, file_name: str, folder: str, content_type: str="image/png")->str:
    """Uploads an image to ImageKit and returns the CDN URL."""
    result = imagekit.files.upload(
        file=(file_bytes, file_name, content_type),
        file_name=file_name,
        folder=folder,
        is_private_file=False,
        use_unique_file_name=True
        )   
    return result.url

def get_variants(image_url: str)->list:
    """Return 3 sizes variant urls using imagekit transformation"""
    return {
        "youtube": f"{image_url}?tr=w-1280,h-720,c-maintain_ratio,fo-auto",
        "shorts": f"{image_url}?tr=w-1080,h-1920,c-maintain_ratio,fo-auto",
        "square": f"{image_url}?tr=w-1080,h-1080,c-maintain_ratio,fo-auto",
    }






