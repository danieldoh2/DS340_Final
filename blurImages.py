from PIL import Image, ImageFilter
import numpy as np
import os

def blur_images(inputFolder, outputFolder): #outputFolder does not need to exist, just name it in function call
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    
    imgFiles = os.listdir(inputFolder)
    
    for file in imgFiles:
        if file == ".DS_Store":
            continue
        blurredFileName = os.path.splitext(file)[0] + 'b' + os.path.splitext(file)[1]
        
        imgPath = os.path.join(inputFolder, file)
        image = Image.open(imgPath)
        blurredImage = image.filter(ImageFilter.GaussianBlur(np.random.randint(3, 10)))
        output_path = os.path.join(outputFolder, blurredFileName)
        blurredImage.save(output_path)
        
    print("Finished blurring images.")
blur_images("./test", "./test-blurred")