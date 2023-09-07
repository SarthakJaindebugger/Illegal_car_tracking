import subprocess
import random
import string
import cv2
import time

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
    cap = cv2.VideoCapture(0)  # Open the default camera (index 0)

    if not cap.isOpened():
        print("Error: Camera not opened.")
        exit()

    # Allow the camera some time to initialize
    time.sleep(2)

    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        
        if not ret:
            print("Error: Could not read frame.")
            break
        
        cv2.imshow('Webcam', frame)  # Display the frame
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('c'):  # Press 'c' to capture the image
            random_suffix = generate_random_string(6)
            image_path = f"captured_{random_suffix}.jpg"
            cv2.imwrite(image_path, frame)  # Save the captured image
            
            output_path = f"out_{random_suffix}.txt"
            psm = 6
            
            saved_file_path = run_tesseract(image_path, output_path, psm)
            
            if saved_file_path:
                contents = read_saved_file(saved_file_path)
                if contents:
                    print("Contents of saved file:")
                    print(contents)
        
        elif key == 27:  # Press 'Esc' to exit
            break
    
    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all OpenCV windows
