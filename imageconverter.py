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


def createtempimg(imgpath):
	i=io.imread(imgpath)
	img=color.rgb2gray(i)
#	imgd=transform.rescale(img, 0.25)
	imgsobel=filters.sobel(img)
	imgsobelexp=exposure.equalize_adapthist(imgsobel)
	imgcanny=feature.canny(img,sigma=2.5)
	imgblended = imgsobelexp+imgcanny

	patharray=imgpath.split('/')
	imgnameparts=patharray[-1].split('.')
	imgpath='/'.join(patharray[0:-1])+'/'+'.'.join(imgnameparts[0:-1])+'BW'
	plt.imsave(imgpath,imgblended,cmap="gray")
	return

with concurrent.futures.ProcessPoolExecutor() as executor:
	dirpath = sys.argv[1]
	paths = glob.glob(dirpath+'*')

	for image_file in zip(paths, executor.map(createtempimg, paths)):
		continue

