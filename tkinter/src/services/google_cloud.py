import requests
from PIL import Image
from io import BytesIO

from src.environments.environments import URL_GOOGLE_CLOUD

def get_image(image):
    url = URL_GOOGLE_CLOUD+image
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        print("Error al obtener la imagen")