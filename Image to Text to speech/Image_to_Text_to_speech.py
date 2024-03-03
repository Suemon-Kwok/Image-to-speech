from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import pytesseract
import pyttsx3
import tkinter as tk

def convert_image_to_text(image_path):
    # Load the image from the path
    image = Image.open(image_path)

    # Use pytesseract to convert the image to text
    text = pytesseract.image_to_string(image)

    return text

def convert_text_to_speech(text):
    # Initialize the speech engine
    engine = pyttsx3.init()

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def drop(event):
    # Get the path of the dropped file
    file_path = event.data.strip('{}')

    # Convert the image in the file to text
    text = convert_image_to_text(file_path)

    # Open the image file
    with Image.open(file_path) as img:
        # Resize the image to fit the label
        img.thumbnail((label.winfo_width(), label.winfo_height()))

        # Convert the Image object to a PhotoImage object
        photo = ImageTk.PhotoImage(img)

        # Update the label's image
        label.config(image=photo)
        label.image = photo  # Keep a reference to the image to prevent it from being garbage collected

    # Convert the text to speech after a delay
    root.after(1000, convert_text_to_speech, text)  # Delay of 1000 milliseconds (1 second)

root = TkinterDnD.Tk()
root.geometry('800x600')

# Create a label widget
label = tk.Label(root, text='Drag and Drop Image Here')
label.pack(fill=tk.BOTH, expand=1)

# Register the label as a drop target for files
label.drop_target_register(DND_FILES)

# Bind the drop event to the drop function
label.dnd_bind('<<Drop>>', drop)

root.mainloop()
