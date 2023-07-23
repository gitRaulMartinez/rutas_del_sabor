import os

def path_images(image):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), image)
