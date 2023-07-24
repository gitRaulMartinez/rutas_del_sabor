import os

from src.assets.assets import FILE

def get_image_path(image):
    return os.path.join(os.path.dirname(os.path.realpath(FILE)), "images", image)