import sys
import numpy
import scipy
import os
import glob
import skimage
from skimage import io,transform, color, feature, filters, exposure
import cv2
from matplotlib import pyplot as plt
import concurrent
from concurrent import futures

#function to convert image to black and white template image
def createtempimg(imgpath):
	i=io.imread(imgpath) #read image from path
	img=color.rgb2gray(i) #convert to grayscale
#	imgd=transform.rescale(img, 0.25)
	imgsobel=filters.sobel(img) #apply sobel filter
	imgsobelexp=exposure.equalize_adapthist(imgsobel) #histogram equalization for better dynamic range
	imgcanny=feature.canny(img,sigma=2.5) #apply canny edge detection
	imgblended = imgsobelexp+imgcanny #combine sobel and canny results for final template image
	
	#naming conventions follow
	patharray=imgpath.split('/')
	imgnameparts=patharray[-1].split('.')
	imgpath='/'.join(patharray[0:-1])+'/'+'.'.join(imgnameparts[0:-1])+'BW'
	plt.imsave(imgpath,imgblended,cmap="gray") #save image in same folder with new name
	return

#code for parallel execution follows
with concurrent.futures.ProcessPoolExecutor() as executor:
	dirpath = sys.argv[1]
	paths = glob.glob(dirpath+'*')

	for image_file in zip(paths, executor.map(createtempimg, paths)):
		continue

