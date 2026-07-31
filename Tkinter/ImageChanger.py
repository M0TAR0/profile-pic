import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

load_dotenv()
current_image = "first"


def change_images():
    global current_image
    if current_image == "first":
        picture.config(image=second_picture)
        pictureTitleLabel.config(text=f"Title: {second_pictureTitle}")
        pictureSizeLabel.config(text=f"Size: {second_pictureSize}")
        pictureFormatLabel.config(text=f"Format: {second_pictureFormat}")
        current_image = "second"
    else:
        picture.config(image=first_picture)
        pictureTitleLabel.config(text=f"Title: {first_pictureTitle}")
        pictureSizeLabel.config(text=f"Size: {first_pictureSize}")
        pictureFormatLabel.config(text=f"Format: {first_pictureFormat}")
        current_image = "first"


canva_size = (1000, 1000)

root = tk.Tk()

# ---SETUP IMAGES

first_image = Image.open(os.getenv("IMAGE_3"))  # type: ignore
first_image.thumbnail(canva_size, Image.Resampling.LANCZOS)
second_image = Image.open(os.getenv("IMAGE_4"))  # type: ignore
second_image.thumbnail((canva_size), Image.Resampling.LANCZOS)


first_picture = ImageTk.PhotoImage(first_image)
first_pictureTitle = "A BEEEEEEEEE.....!"
first_pictureSize = str(first_image.size)
first_pictureFormat = str(first_image.format)

second_picture = ImageTk.PhotoImage(second_image)
second_pictureTitle = "A Nice Flower!"
second_pictureSize = str(second_image.size)
second_pictureFormat = str(second_image.format)


# ---SETUP TKINTER
root.title("IMAGE MAGIC!")
root.geometry(f"{canva_size[0] + 200}x{canva_size[1] + 300}")

mainframe = ttk.Frame(root, padding=20)
mainframe.grid(column=0, row=0, sticky=("N", "W", "E", "S"))

titleLabel = ttk.Label(
    mainframe, text="WELCOME TO THE IMAGE CHANGER", font=("Arial", 13, "bold")
)
titleLabel.grid(column=2, row=1, sticky=("N", "S"), pady=20)

informationFrame = ttk.Frame(mainframe, padding=5)
informationFrame.grid(column=1, row=2, sticky=("N", "S"))

pictureTitleLabel = ttk.Label(
    informationFrame, text=f"Title: {first_pictureTitle}", padding=5
)
pictureTitleLabel.grid(row=0, sticky="S", pady=10)
pictureSizeLabel = ttk.Label(
    informationFrame, text=f"Size: {first_pictureSize}", padding=5
)
pictureSizeLabel.grid(row=1, sticky=("N", "S"), pady=10)
pictureFormatLabel = ttk.Label(
    informationFrame, text=f"Format: {first_pictureFormat}", padding=5
)
pictureFormatLabel.grid(row=2, sticky="N", pady=10)

picture = ttk.Label(mainframe, image=first_picture)
picture.grid(column=2, row=2, sticky=("W", "E"))

change_button = ttk.Button(
    mainframe, text="Click to change!", command=change_images, padding=20
)
change_button.grid(column=2, row=3, sticky=("N", "S"), pady=20)

for i in range(0, 3):
    informationFrame.rowconfigure(i, weight=1)
# --- RUN TKINTER
root.mainloop()
