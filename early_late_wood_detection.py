from PIL import Image, ImageEnhance
import os
from os import listdir
folder_dir = "./images"
for image in os.listdir(folder_dir):
    im = Image.open(folder_dir + "/" + image).convert("L") 
    enhancer = ImageEnhance.Contrast(im)
    factor = 100
    im_output = enhancer.enhance(factor)
    
    pix_val = list(im_output.getdata())

    total_white_pixels = 0
    total_black_pixels = 0
    for pixel in pix_val:
        if pixel > 125:
            total_white_pixels += 1
        else:
            total_black_pixels += 1
    ratio = total_black_pixels / (total_white_pixels + total_black_pixels)
    
    # print the early/latewood ration
    print("latewood ratio: " + "%.3f" % ratio + " earlywood ratio: " + "%.3f" % (1 - ratio) + " " + str(image))    
    # show black white image
    #im.show()
    
    # show greyscale image
    #im_output.show()