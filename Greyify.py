from PIL import Image
import os

def grayscale(path):
    for filename in os.listdir(path):
        img = Image.open(path + filename).convert('L')
        os.remove(path + filename)
        img.save(path + filename)
