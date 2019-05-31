import os
from PIL import Image

def splitPosNeg(path, seed, categories = ['pos', 'neg']):
    os.mkdir(path + 'all')

    filestring = ''
    categoryCount = 0
    dataCount = seed

    for category in categories:
        for filename in os.listdir(path + category + '/'):
          os.rename(path + category + '/' + filename, path + 'all/' + str(dataCount) + '.' + filename.split('.')[1])
          filestring += str(categoryCount) + ',';
          dataCount += 1
        categoryCount += 1
        os.rmdir(path + category + '/')
    
    filestring = filestring[:-1]
    with open(path + 'Lables.txt', 'w') as f:
      f.write(filestring)

# grayscale and set to 64x64 pixels
def standardize(path):
    for filename in os.listdir(path):
        img = Image.open(path + filename).convert('L').resize( (64, 64) , Image.ANTIALIAS) # .convert('L') grayscales the image
        img.save(path + filename)

def clean(path, seed):
    splitPosNeg(path, seed)
    standardize(path + "all/")
