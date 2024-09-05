
from tkinter import *
from tkinter import messagebox
import base64
import secrets
import string

def generate_strong_key(length=20):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

# Initialize the root window
root = Tk()

# Initialize StringVar variables
message_var = StringVar()
private_key = StringVar(value=generate_strong_key())  # Default private key
mode = StringVar(value="Encode")  # Default mode set to Encode
result_var = StringVar()

# List to store message history
history = []

# Encode function
def Encode(key, message):
    try:
        enc = [chr((ord(message[i]) + ord(key[i % len(key)])) % 256) for i in range(len(message))]
        encoded_message = base64.urlsafe_b64encode("".join(enc).encode()).decode()
        
        # Add to history
        history.append(f"Mode: Encode\nKey: {key}\nMessage: {message}\nEncoded: {encoded_message}")
        update_history()
        
        return encoded_message
    
    except Exception as e:
        messagebox.showerror("Encoding Error", f"An error occurred while encoding: {str(e)}")
        message_var.set("")  # Clear text box
        result_var.set("")  # Clear result box
        return ""

# Decode function
def Decode(key, message):
    try:
        message = base64.urlsafe_b64decode(message).decode()
        dec = [chr((256 + ord(message[i]) - ord(key[i % len(key)])) % 256) for i in range(len(message))]
        decoded_message = "".join(dec)
        
        # Add to history
        history.append(f"Mode: Decode\nKey: {key}\nMessage: {message}\nDecoded: {decoded_message}")
        update_history()
        
        return decoded_message
    
    except base64.binascii.Error: #Not an encoded message
        messagebox.showerror("Decoding Error", "Please enter an encoded message to start decoding")
        message_var.set("")  # Clear text box
        result_var.set("")  # Clear result box
        
    except Exception as e:
        messagebox.showerror("Decoding Error", f"Please enter an encoded message to start decoding.\nAn error occurred while decoding: {str(e)}")
        message_var.set("")  # Clear text box
        result_var.set("")  # Clear result box
        
    return ""

# Function to encode or decode based on mode
def Mode():
    # Check if message or key is empty
    if not message_var.get() or not private_key.get():
        messagebox.showerror("Input Error", "Please enter message / key.")
        return

    if mode.get() == 'Encode':
        result_var.set(Encode(private_key.get(), message_var.get()))
        
    elif mode.get() == 'Decode':
        result_var.set(Decode(private_key.get(), message_var.get()))
        
    else:
        result_var.set('Invalid Mode')

# Function to reset fields
def Reset():
    message_var.set("")
    private_key.set(generate_strong_key())
    mode.set("Encode")
    result_var.set("")

# Function to exit the application
def Exit():
    root.destroy()

# Function to update the history
def update_history():
    history_text = "\n\n".join(history[-10:])  # Show last 10 entries
    history_panel.config(state=NORMAL)
    history_panel.delete(1.0, END)
    history_panel.insert(INSERT, history_text)
    history_panel.config(state=DISABLED)
