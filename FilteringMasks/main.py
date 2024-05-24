# A program to compare the pixel value of two IMAGE, where IMAGE:
# is a square matrix of pixels representing UV maps
# is a black image where the values of 1 represent positions where bumps or high topologies are found

# MODULES
import cv2
import numpy as np


# FD. readImage()
# purp. read an image with a threshold value
# INVARIANT: one of the images is the mask that is already binary. The other may vary depending on the threshold value
def readImage(name:str):
    image = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
    threshold_value = 50  # Threshold value
    max_value = 255  # Maximum value to use with the THRESH_BINARY thresholding type
    ret, binaryImage = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)
    return binaryImage


# DD
# DD. IMAGE
# image = numpy.array()
image1 = readImage("mask1.png")
image2 = readImage("mask2.png")



# CODE

# for every pixel:
# if there is a value > 0 in the mask 1 AND mask2, set the value to 1
# Check if both images have the same shape
if image1.shape == image2.shape:
    # Perform the AND operation
    and_image = np.bitwise_and(image1, image2)
    print(np.max(and_image))
    cv2.imwrite("mask_filtered.png",and_image)
    # Display the original and thresholded images
    # cv2.imshow('Grayscale Image', and_image)
    # cv2.imshow('Binary Image', image1)
    # cv2.imshow('Binary Image', image2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
