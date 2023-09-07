
'''
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pytesseract
import imutils

# Read image
img = cv2.imread('/Users/sarthakjain/Desktop/ANPRwithPython-main/image4.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply filters
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
edged = cv2.Canny(bfilter, 30, 200)  # Edge detection

# Find contours and location of license plate
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

# Create a mask to isolate the license plate
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

# Crop the license plate
(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(y), np.min(x))
(x2, y2) = (np.max(y), np.max(x))
cropped_image = gray[y1:y2 + 1, x1:x2 + 1]

# Use Tesseract to extract text
extracted_text = pytesseract.image_to_string(cropped_image)

# Rendering
text = extracted_text
font = cv2.FONT_HERSHEY_SIMPLEX
res = cv2.putText(img, text=text, org=(location[0][0][0], location[1][0][1] + 60), fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
res = cv2.rectangle(img, tuple(location[0][0]), tuple(location[2][0]), (0, 255, 0), 3)

# Resize the image using OpenCV's interpolation method
width, height = 250, 250
img_resized = cv2.resize(img, (width, height))

# Display the original and processed images
plt.figure(figsize=(12, 6))

#plt.subplot(1, 2, 1)
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB))
plt.title("Processed Image")

plt.show()
'''


import cv2
from matplotlib import pyplot as plt
import numpy as np
import pytesseract
import imutils
import re

# Read image
img = cv2.imread('/Users/sarthakjain/Desktop/ANPRwithPython-main/image1.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply filters
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
edged = cv2.Canny(bfilter, 30, 200)  # Edge detection

# Find contours and location of license plate
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

# Create a mask to isolate the license plate
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

# Crop the license plate
(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(y), np.min(x))
(x2, y2) = (np.max(y), np.max(x))
cropped_image = gray[y1:y2 + 1, x1:x2 + 1]

# Use Tesseract to extract text
extracted_text = pytesseract.image_to_string(cropped_image)

# Extract only alphabets and numbers using regular expression
number_plate_number = re.sub(r'[^a-zA-Z0-9]', '', extracted_text)

# Rendering
text = number_plate_number
font = cv2.FONT_HERSHEY_SIMPLEX
res = cv2.putText(img, text=text, org=(location[0][0][0], location[1][0][1] + 60), fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
res = cv2.rectangle(img, tuple(location[0][0]), tuple(location[2][0]), (0, 255, 0), 3)

# Resize the image using OpenCV's interpolation method
width, height = 250, 250
img_resized = cv2.resize(img, (width, height))

# Print the extracted number plate number
print("Extracted Number Plate Number:", number_plate_number)

# Display the original and processed images
plt.figure(figsize=(12, 6))

# plt.subplot(1, 2, 1)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB))
plt.title("Processed Image")

plt.show()

