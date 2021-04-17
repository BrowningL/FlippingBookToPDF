from PIL import Image
import os
import os.path
import glob
from natsort import natsorted

#Create first variable to be turned into PDF
im1 = Image.open(r'C:\Users\Lukem\Documents\AutomaticTextbook\PageNumber1.png')

imagelist = []

#Function to create a list of all current png files stored in python directory
def databaseList():
    fileList = glob.glob((os.getcwd()) + "/*.png") # Include slash or it will search in the wrong directory!!
    fileList = natsorted(fileList)  #Sorts file paths
    for file in fileList:
        fileNew = Image.open(file)
        imagelist.append(fileNew)
    return()

databaseList()
#Gets rid of first page in list to make up for im1 variable
imagelist.pop(0)
#This will bring it all together into a PDF file
im1.save(r'C:\Users\Lukem\Documents\AutomaticTextbook\myImages.pdf', save_all=True, append_images=imagelist)
