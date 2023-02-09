#Import required libraries
import cv2
import numpy as np

#Get the image path from the user
img_path = input("Enter the image path: ")

#Load the image
img = cv2.imread(img_path)
cv2.imshow("Original Image", img)
#Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Apply Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (5,5), 0)

#Perform binary thresholding to segment the defects
_, threshold = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)

#Find the contours in the thresholded image
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Draw the contours on the original image
cv2.drawContours(img, contours, -1, (0,0,255), 2)

#Loop through the contours to find and mask the defect regions
for contour in contours:
    mask = np.zeros(img.shape[:2], dtype="uint8")
    cv2.drawContours(mask,[contour],-1, 255, -1)
    masked = cv2.bitwise_and(img, img, mask=mask)

#Show the results
cv2.imshow("Resulted Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
