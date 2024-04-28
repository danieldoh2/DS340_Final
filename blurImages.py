from PIL import Image, ImageFilter
import numpy as np
import os

def blur_images(inputFolder, outputFolder): #outputFolder does not need to exist, just name it in function call
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    
    imgFiles = os.listdir(inputFolder)
    
    for file in imgFiles:
        imgPath = os.path.join(inputFolder, file)
        image = Image.open(imgPath)
        blurredImage = image.filter(ImageFilter.GaussianBlur(np.random.randint(3, 10)))
        output_path = os.path.join(outputFolder, file)
        blurredImage.save(output_path)
        
    print("Finished blurring images.")
blur_images("./images_to_blur", "./blurred_images")