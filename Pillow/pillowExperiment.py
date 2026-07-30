import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
IMAGE1 = os.getenv("IMAGE_1")
IMAGE2 = os.getenv("IMAGE_2")
IMAGE3 = os.getenv("IMAGE_3")
IMAGE4 = os.getenv("IMAGE_4")
FINAL_IMAGE = os.getenv("IMAGE_FINAL")

# LOADING IMAGES
img_1 = Image.open(IMAGE1)  # type: ignore
img_2 = Image.open(IMAGE2)  # type: ignore
img_3 = Image.new("RGB", (500, 500), "white")

# SHOWING IMAGES
# img_1.show()
# img_2.show()
# img_3.show()

# PRINTING DETAILS
print("IMAGE #1:")
print("Size:  ", img_1.size)
print(f"Type:  {img_1.format}")
print("Mode :  ", img_1.mode)

print("\n\n")

print("IMAGE #2:")
print("Size:  ", img_2.size)
print(f"Type:  {img_2.format}")
print("Mode:  ", img_2.mode)

print("\n\n")

print("IMAGE #3:")
print("Size:  ", img_3.size)
print(f"Type:  {img_3.format}")
print("Mode:  ", img_3.mode)

# IMAGE MANIPULATION
img_4 = img_1.rotate(45)
img_5 = img_1.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT).transpose(
    method=Image.Transpose.FLIP_TOP_BOTTOM
)
img_6 = img_1.crop((200, 200, 1000, 1000))

# img_4.show()
# img_5.show()
# img_6.show()

# COLOR CONVERSION
img_7 = img_2.convert("L")
img_8 = img_2.convert("RGBA")
img_9 = img_2.convert("1")


# img_7.show()
# img_8.show()
# img_9.show()


# PASTING IMAGES
img_10 = Image.new("RGB", (4500, 3000), "white")
img_10.paste(img_1, (0, 0))
img_10.paste(img_2, (2500, 700))
img_10.paste(img_6, (1000, 1000))

# img_10.show()

# FINAL IMAGE
img_11 = Image.new("RGB", (5760, 5760), "white")
img_6 = img_6.resize((1920, 1920))

img_11.paste(img_1, (0, 0))
img_11.paste(img_2, (1920, 0))
img_11.paste(img_3, (3840, 0))
img_11.paste(img_4, (0, 1920))
img_11.paste(img_5, (1920, 1920))
img_11.paste(img_6, (3840, 1920))
img_11.paste(img_7, (0, 3840))
img_11.paste(img_8, (1920, 3840))
img_11.paste(img_9, (3840, 3840))

img_11.show()
img_11.save(FINAL_IMAGE)  # type: ignore
