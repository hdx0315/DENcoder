
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


###########################################################################################3
##### GUI #####

# Set up the GUI window
root.geometry('850x550')
root.title("DENcoder - Decoder & Encoder")


# Frame for input and buttons
input_frame = Frame(root, width=500)
input_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
input_frame.pack_propagate(False)  # Prevent frame from resizing beyond set width

# Frame for history
history_frame = Frame(root, width=350, bg='lightgrey')
history_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)
history_frame.pack_propagate(False)



# Elements in the input frame

# Main title
Label(input_frame, text='DENcoder', font='arial 20 bold').pack(pady=10)

# Input fields
# Message
Label(input_frame, font='arial 12 bold', text='MESSAGE').pack(anchor=W, padx=10, pady=5)
Entry(input_frame, font='arial 10', textvariable=message_var, bg='ghost white').pack(fill=X, padx=20)
Label(input_frame).pack(pady=3) 


# Private Key
Label(input_frame, font='arial 12 bold', text='KEY').pack(anchor=W, padx=10, pady=5)
Entry(input_frame, font='arial 10', textvariable=private_key, bg='ghost white').pack(fill=X, padx=20)
Label(input_frame).pack(pady=3) 

 
# Mode
Label(input_frame, font='arial 12 bold', text='MODE').pack(anchor=W, padx=10, pady=5)
# Dropdown Menu
OptionMenu(input_frame, mode, "Encode", "Decode").pack(fill=X, padx=20)
Label(input_frame).pack(pady=3) 

 
# Result Output Panel
Entry(input_frame, font='arial 10 bold', textvariable=result_var, bg='ghost white', state='readonly').pack(fill=X, padx=20, pady=10)


# Result button
Button(input_frame, font='arial 10 bold', text='RESULT', padx=10, bg='LightGray', command=Mode).pack(pady=5)


# Reset and Exit buttons
Button(input_frame, font='arial 10 bold', text='RESET', width=10, command=Reset, bg='LimeGreen').pack(side=LEFT, padx=35, pady=5)
Button(input_frame, font='arial 10 bold', text='EXIT', width=10, command=Exit, bg='OrangeRed').pack(side=RIGHT, padx=35, pady=5)


# Bottom label
Label(input_frame, text='--hdx0315--', font='arial 8').pack(side=BOTTOM)  



# History panel on the right side

# Top Title
history_title = Label(history_frame, text='History', font='arial 12 bold', bg='lightgrey')
history_title.pack(pady=10)

# Area to display history
history_panel = Text(history_frame, font='arial 10', bg='white', wrap=WORD, state=DISABLED)
history_panel.pack(expand=True, fill=BOTH, padx=10, pady=10)


# Update history panel initially
update_history()


# Start the main loop
root.mainloop()
