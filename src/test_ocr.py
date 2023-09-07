
'''
from PIL import Image
import pytesseract

# Extract text from the image
extracted_text = pytesseract.image_to_string('/Users/sarthakjain/Desktop/ML Projects/Car_monitoring system/img/10.jpeg')

# Write the extracted text to a file
with open('extracted_text.txt', 'w') as f:
    f.write(extracted_text)
'''



'''

import subprocess

def run_tesseract(image_path, output_path, psm=6):
    try:
        tesseract_path = '/usr/local/bin/tesseract'  # Replace this with the actual path to the tesseract executable
        
        command = [
            tesseract_path,
            image_path,
            output_path,
            '--psm', str(psm)
        ]
        
        # Run the Tesseract command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Print captured standard output
        print("Tesseract output:")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        # Print error message if the command fails
        print("Error:", e)
        print("Tesseract error output:")
        print(e.stderr)

if __name__ == "__main__":
    image_path = "/Users/sarthakjain/Desktop/ML Projects/Car_monitoring system/img/15.png"   # Path to your image
    output_path = "out1.txt"  # Path to the output file
    psm = 6  # Page segmentation mode
    
    run_tesseract(image_path, output_path, psm)
'''



import subprocess
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def run_tesseract(image_path, output_path, psm=6):
    try:
        tesseract_path = '/usr/local/bin/tesseract'  # Replace this with the actual path to the tesseract executable
        
        command = [
            tesseract_path,
            image_path,
            output_path,
            '--psm', str(psm)
        ]
        
        # Run the Tesseract command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Print captured standard output
        print("Tesseract output:")
        print(result.stdout)
        
        return output_path  # Return the path to the saved file
        
    except subprocess.CalledProcessError as e:
        # Print error message if the command fails
        print("Error:", e)
        print("Tesseract error output:")
        print(e.stderr)
        return None

def read_saved_file(file_path):
    try:
        with open((file_path + ".txt"), 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print("File not found:", file_path)
        return None

if __name__ == "__main__":
    image_path = "/Users/sarthakjain/Desktop/ML Projects/Car_monitoring system/img/1.jpeg"   # Path to your image
    random_suffix = generate_random_string(6)  # Generate a random string with 6 characters
    output_path = f"out_{random_suffix}.txt"  # Construct the output file path with random suffix
    psm = 6  # Page segmentation mode
    
    saved_file_path = run_tesseract(image_path, output_path, psm)
    
    if saved_file_path:
        contents = read_saved_file(saved_file_path)
        if contents:
            print("Contents of saved file:")
            print(contents)
