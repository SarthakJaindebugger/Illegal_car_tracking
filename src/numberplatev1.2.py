'''
import cv2
import numpy as np
import pytesseract
import imutils
import re
import os

# Path to the video file
video_path = '/Users/sarthakjain/Desktop/video2.mp4'
output_directory = '/Users/sarthakjain/Desktop/ML Projects/Car_monitoring system/img'

# Create a VideoCapture object
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply filters
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
    edged = cv2.Canny(bfilter, 30, 200)  # Edge detection

    # Find contours and location of license plate
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = tuple(approx[0][0])  # Convert to tuple

            if cv2.contourArea(contour) < 50:  # Adjust threshold as needed
                continue

            # Create a mask to isolate the license plate
            mask = np.zeros(gray.shape, np.uint8)
            new_image = cv2.drawContours(mask, [approx], 0, 255, -1)
            new_image = cv2.bitwise_and(frame, frame, mask=mask)

            # Crop the license plate
            (x, y) = np.where(mask == 255)
            (x1, y1) = (np.min(y), np.min(x))
            (x2, y2) = (np.max(y), np.max(x))
            cropped_image = gray[y1:y2 + 1, x1:x2 + 1]

            # Draw bounding box around license plate
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)

            # Use Tesseract to extract text
            extracted_text = pytesseract.image_to_string(cropped_image)

            # Extract only alphabets and numbers using regular expression
            number_plate_number = re.sub(r'[^a-zA-Z0-9]', '', extracted_text)

            if number_plate_number:
                # Print the detected number plate number on the frame
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, text=number_plate_number, org=(x1, y1 - 10), fontFace=font, fontScale=0.6, color=(0, 255, 0), thickness=2)

                # Save the captured license plate image to the output directory
                plate_filename = os.path.join(output_directory, f'plate_{number_plate_number}.png')
                cv2.imwrite(plate_filename, cropped_image)

    # Display the processed frame
    cv2.imshow('Processed Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all windows
cap.release()
cv2.destroyAllWindows()
'''

'''

import cv2
import numpy as np
import pytesseract
import imutils
import re
import os

# Path to the video file
video_path = '/Users/sarthakjain/Desktop/video2.mp4'
output_directory = '/Users/sarthakjain/Desktop/ML Projects/Car_monitoring system/img'

# Create a VideoCapture object
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply filters
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
    edged = cv2.Canny(bfilter, 30, 200)  # Edge detection

    # Find contours and location of license plate
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = tuple(approx[0][0])  # Convert to tuple

            if cv2.contourArea(contour) < 50:  # Adjust threshold as needed
                continue

            # Create a mask to isolate the license plate
            mask = np.zeros(gray.shape, np.uint8)
            new_image = cv2.drawContours(mask, [approx], 0, 255, -1)
            new_image = cv2.bitwise_and(frame, frame, mask=mask)

            # Crop the license plate
            (x, y) = np.where(mask == 255)
            (x1, y1) = (np.min(y), np.min(x))
            (x2, y2) = (np.max(y), np.max(x))
            cropped_image = gray[y1:y2 + 1, x1:x2 + 1]

            # Draw bounding box around license plate
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)

            # Use Tesseract to extract text
            extracted_text = pytesseract.image_to_string(cropped_image)

            # Extract only alphabets and numbers using regular expression
            number_plate_number = re.sub(r'[^a-zA-Z0-9]', '', extracted_text)

            if number_plate_number:
                # Print the detected number plate number on the frame
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, text=number_plate_number, org=(x1, y1 - 10), fontFace=font, fontScale=0.6, color=(0, 255, 0), thickness=2)

                # Print the extracted text to console
                print("Detected Number Plate Text:", extracted_text)

                # Save the captured license plate image to the output directory
                plate_filename = os.path.join(output_directory, f'plate_{number_plate_number}.png')
                cv2.imwrite(plate_filename, cropped_image)

    # Display the processed frame
    cv2.imshow('Processed Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all windows
cap.release()
cv2.destroyAllWindows()
'''


import cv2
import numpy as np
import pytesseract
import imutils
import re
import os

# List of valid state codes
states = ['AP', 'AR', 'AS', 'BR', 'CG', 'DL', 'GA', 'GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LD', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TS', 'TR', 'UP', 'UK', 'WB', 'AN', 'CH', 'DN', 'DD', 'LA']

# Path to the video file
video_path = '/Users/sarthakjain/Desktop/video2.mp4'
output_directory = '/Users/sarthakjain/Desktop/ML Projects/Car_monitoring system/img'
# Create a VideoCapture object
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply filters
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
    edged = cv2.Canny(bfilter, 30, 200)  # Edge detection

    # Find contours and location of license plate
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = tuple(approx[0][0])  # Convert to tuple

            if cv2.contourArea(contour) < 50:  # Adjust threshold as needed
                continue

            # Create a mask to isolate the license plate
            mask = np.zeros(gray.shape, np.uint8)
            new_image = cv2.drawContours(mask, [approx], 0, 255, -1)
            new_image = cv2.bitwise_and(frame, frame, mask=mask)

            # Crop the license plate
            (x, y) = np.where(mask == 255)
            (x1, y1) = (np.min(y), np.min(x))
            (x2, y2) = (np.max(y), np.max(x))
            cropped_image = gray[y1:y2 + 1, x1:x2 + 1]

            # Draw bounding box around license plate
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)

            # Use Tesseract to extract text
            extracted_text = pytesseract.image_to_string(cropped_image)

            # Extract only alphanumeric characters with length of 10 and no spaces
            number_plate_number = re.sub(r'[^a-zA-Z0-9]', '', extracted_text)

            if len(number_plate_number) == 10 and number_plate_number[-4:].isdigit() and number_plate_number.isupper() and number_plate_number[:2] in states:
                # Print the detected number plate number on the frame
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, text=number_plate_number, org=(x1, y1 - 10), fontFace=font, fontScale=0.6, color=(0, 255, 0), thickness=2)

                # Print the extracted text to console
                print("Detected Number Plate Text:", number_plate_number)

                # Save the captured license plate image to the output directory
                plate_filename = os.path.join(output_directory, f'plate_{number_plate_number}.png')
                cv2.imwrite(plate_filename, cropped_image)

    # Display the processed frame
    cv2.imshow('Processed Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all windows
cap.release()
cv2.destroyAllWindows()
