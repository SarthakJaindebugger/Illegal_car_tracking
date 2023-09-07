#ACCOUNT_SID = "AC9ff95645f4d90ba75da1577439cb3387"
#AUTH_TOKEN = "47975eb06128cfe56cfa272db0159046"
#+18506603149


import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client
import random

# Replace these with your actual Twilio credentials
ACCOUNT_SID = "AC9ff95645f4d90ba75da1577439cb3387"
AUTH_TOKEN = "47975eb06128cfe56cfa272db0159046"

def generate_otp():
    # Generate a random 6-digit OTP
    return str(random.randint(1000, 9999))

def submit():
    global otp

    mobile_number = country_code.get() + " " + mobile_number_entry.get()
    user_otp = otp_entry.get()

    # Verify the entered OTP with the generated OTP
    if user_otp == otp:
        stop_timer()
        messagebox.showinfo("Success", "OTP Verified Successfully!")
    else:
        messagebox.showerror("Error", "Invalid OTP. Please try again.")

def resend(event=None):  # Use event=None to allow both button click and Enter key press
    global otp
    stop_timer()
    otp = generate_otp()
    start_timer()

    # Send the new OTP to the user's mobile number using Twilio
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(
            to=country_code.get() + " " + mobile_number_entry.get(),
            from_="+18506603149",
            body=f"Your OTP is: {otp}"
        )
        messagebox.showinfo("Resend OTP", "New OTP sent to your mobile number.")
    except Exception as e:
        messagebox.showerror("Twilio Error", f"Failed to send OTP: {str(e)}")

def start_timer():
    global remaining_time, otp
    remaining_time = 300  # 5 minutes in seconds
    otp = generate_otp()  # Generate a new OTP
    update_timer()

def update_timer():
    global remaining_time
    if remaining_time > 0:
        minutes, seconds = divmod(remaining_time, 60)
        timer_label.config(text=f"Time Left: {minutes:02d}:{seconds:02d}")
        remaining_time -= 1
        root.after(1000, update_timer)  # Schedule the function after 1000ms (1 second)
    else:
        timer_label.config(text="OTP Expired", fg="red")

def stop_timer():
    global remaining_time
    remaining_time = 0

# Create the main tkinter window
root = tk.Tk()
root.title("OTP Verification")
root.geometry("400x300")  # Set the size of the tkinter window

# Create a StringVar for the country code with a default value of "+91"
country_code = tk.StringVar(value="+91")

# Create labels and input fields
country_code_label = tk.Label(root, text="Country Code:")
country_code_label.pack()
country_code_entry = tk.Entry(root, textvariable=country_code, bd=3)  # Add a white border (bd) to the entry widget
country_code_entry.pack()

mobile_number_label = tk.Label(root, text="Enter Mobile Number:")
mobile_number_label.pack()
mobile_number_entry = tk.Entry(root, bd=3)  # Add a white border (bd) to the entry widget
mobile_number_entry.pack()

otp_label = tk.Label(root, text="Enter OTP:")
otp_label.pack()
otp_entry = tk.Entry(root, bd=3)  # Add a white border (bd) to the entry widget
otp_entry.pack()

# Create submit and resend buttons
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

resend_button = tk.Button(root, text="Resend OTP", command=resend)
resend_button.pack()

# Create a label to display the countdown timer
timer_label = tk.Label(root, text="Time Left: 05:00")
timer_label.pack()

# Initialize global variables
remaining_time = 0
otp = ""

# Bind the Enter key event to the "Resend OTP" function
root.bind("<Return>", resend)

# Start the timer when the program starts
start_timer()

# Start the main event loop
root.mainloop()
