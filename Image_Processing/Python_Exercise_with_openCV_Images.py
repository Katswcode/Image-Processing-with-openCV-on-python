# Making an exercise with OpenCV and images, 5 parts

import cv2
import matplotlib.pyplot as plt
import numpy as np
# Variable with the path image
path = r"C:\Users\sebas\Downloads\Pirates.jpeg"
path2 = r"C:\Users\sebas\Downloads\messi.jpg"
# Exercise a. Convert the image to Grayscale

# Read the Image of the path
Image = cv2.imread(path)

# Check if the first image is loaded successfully
if Image is None:
    print("Error: Unable to read the first image.")
    exit()
Image2 = cv2.imread(path2)

# Check if the second image is loaded successfully
if Image2 is None:
    print("Error: Unable to read the second image.")
    exit()
    
# Check if images have valid dimensions
if Image.size == 0 or Image2.size == 0:
    print("Error: One or both images have invalid dimensions.")
    exit()    
# Resize the image to 75% of his width and height
# img_75 = cv2.resize(Image, None, fx = 0.75, fy = 0.75)
# Showing the Original image
# cv2.imshow("Original Image",img_75)
# Converting the image to Grayscale
gray_image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY) 
# Showing the image grayscaled
cv2.imshow("Grayscaled",gray_image)

# Exercise b.  Apply a Gaussian blur to the grayscale image.
# Using blur function to blur the image, 2 parameter is to add more or less blur in the image
Gaussian_blur_image = cv2.GaussianBlur(gray_image,(5,5),0)
# Showing the image grayscaled
cv2.imshow("Image Blurring",Gaussian_blur_image)

# Exercise c. Use Canny edge detection to highlight edges in the blurred image.
# Creating a edge image with Canny function
edges = cv2.Canny(Gaussian_blur_image,100,200)
# Showing the edge image 
cv2.imshow('Edges image', edges)

# Exercise d. Find and draw contours on the original image based on the edges detected.

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Maaking a copy cause if not it would affect to the original image
draw_contour = Image.copy()
# drawing through the copy
cv2.drawContours(draw_contour, contours, -1, (0, 255, 0), 3)
# showing the result
cv2.imshow('Contours image', draw_contour)

# Adding 50 it adjust the image in terms of brightness
addition_matrix = np.ones(Image.shape, dtype="uint8") * 50
# Adding weight to the image because if not it would be saturated
result_image = cv2.addWeighted(Image, 1, np.zeros_like(Image), 0, 50)
# showing the image with the addition
cv2.imshow('addition matrix image', result_image)

# Extra exercise:
# Adding the Image 2 to the Image
if Image.shape[:2] == (0, 0) or Image2.shape[:2] == (0, 0):
    print("Error: One or both images have invalid dimensions.")
    exit()
# Print dimensions before resizing
print("Original Image 1 Dimensions:", Image.shape)
print("Original Image 2 Dimensions:", Image2.shape)    
    
# Realizing an resize for the 2 image cause it didn't work because their dimensions are diferent than the first image
image2_resized = cv2.resize(Image2, (Image.shape[1], Image.shape[0]))
# Print dimensions after resizing
print("Resized Image 2 Dimensions:", image2_resized.shape)
# Check if dimensions are compatible
if Image.shape != image2_resized.shape:
    print("Error: Resized Image 2 dimensions do not match Image 1.")
    exit()

# Add the two resized images together    
# Add the two resized images together using cv2.addWeighted
result_image = cv2.addWeighted(Image, 0.43, image2_resized, 0.57, 0)

# Showing the image 2 resized
cv2.imshow("Image 2 Resized", image2_resized)
# Showing the 2 image original
cv2.imshow("Image 2", Image2)
# Showing the result of add this 2 images
cv2.imshow("Result Image", result_image)
# waiting until the user press any key to avoid Python kernel from crashing
cv2.waitKey(0) 


    
