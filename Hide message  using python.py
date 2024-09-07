from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from stegano import lsb  # Make sure to install the stegano library using pip

# Function to hide a secret message in an image
def hide_message():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", ".png;.jpg;*.jpeg")])
    if image_path:
        secret_message = secret_text.get("1.0", END).strip()
        if secret_message:
            # Hide the message in the image
            secret_image = lsb.hide(image_path, secret_message)
            save_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save Image As", filetypes=[("PNG Files", "*.png")])
            if save_path:
                secret_image.save(save_path)
                result_label.config(text="Message hidden successfully!", fg="green")
        else:
            result_label.config(text="Please enter a message to hide.", fg="red")

# Function to reveal a hidden message from an image
def reveal_message():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", ".png;.jpg;*.jpeg")])
    if image_path:
        hidden_message = lsb.reveal(image_path)
        if hidden_message:
            result_label.config(text=f"Hidden Message: {hidden_message}", fg="cyan")
        else:
            result_label.config(text="No hidden message found.", fg="red")

# Create the main application window
root = Tk()
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("800x600+150+100")
root.resizable(False, False)
root.configure(bg="black")  # Black background

# Create and place widgets with colorful aesthetics
title_label = Label(root, text="Steganography Tool", bg="black", fg="white", font=("Helvetica", 24, "bold"))
title_label.pack(pady=20)

Label(root, text="Enter your secret message:", bg="black", fg="white", font=("Helvetica", 14)).pack(pady=10)

# Create a frame for the text box to simulate rounded corners
text_frame = Frame(root, bg="#333333", bd=2, relief="ridge")  # Dark gray background for the frame
text_frame.pack(pady=10)

secret_text = Text(text_frame, height=5, width=60, font=("Helvetica", 12), wrap=WORD, bg="#1e1e1e", fg="white", bd=0, highlightthickness=0)  # Darker background for Text widget
secret_text.pack(padx=5, pady=5)  # Add padding inside the text box

hide_button = Button(root, text="Hide Message (open folder)", command=hide_message, bg="#4caf50", fg="white", font=("Helvetica", 12, "bold"))
hide_button.pack(pady=10)

reveal_button = Button(root, text="Reveal Message", command=reveal_message, bg="#2196f3", fg="white", font=("Helvetica", 12, "bold"))
reveal_button.pack(pady=10)

result_label = Label(root, text="", bg="black", fg="white", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
