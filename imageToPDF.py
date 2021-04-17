from PIL import Image
import os
import os.path
import glob
from natsort import natsorted

im1 = Image.open(r'C:\Users\Lukem\Documents\AutomaticTextbook\PageNumber1.png')
#image2 = Image.open(r'C:\Users\Lukem\Documents\screenshotDocuments\PageNumber2.png')
#image3 = Image.open(r'C:\Users\Lukem\Documents\screenshotDocuments\PageNumber3.png')
#image4 = Image.open(r'C:\Users\Lukem\Documents\screenshotDocuments\PageNumber4.png')


#im1 = image1.convert('RGB')
#im2 = image2.convert('RGB')
#im3 = image3.convert('RGB')
#im4 = image4.convert('RGB')

imagelist = []



#Function to create a list of all current database files created in order to compare them against username
def databaseList():
    fileList = glob.glob((os.getcwd()) + "/*.png") # Include slash or it will search in the wrong directory!!
    fileList = natsorted(fileList)
    for file in fileList:
        #print(file)
        fileNew = Image.open(file)
        #image = fileNew.convert('RBG')
        imagelist.append(fileNew)
    return()

databaseList()

print(imagelist)

imagelist.pop(0)
im1.save(r'C:\Users\Lukem\Documents\AutomaticTextbook\myImages.pdf', save_all=True, append_images=imagelist)
