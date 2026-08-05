from PIL import Image, ImageDraw
import time

canvas = Image.new("RGB", (400, 400), "White")
profilePicture = ImageDraw.Draw(canvas)

# for i in range(50, 400, 50):
#     profilePicture.line((0, i, 400, i), fill=(100, 100, 100), width=5)
#     canvas.save("Profile_picture.png")
#     time.sleep(0.2)
#     # profilePicture.line((0, i + 1, 400, i + 1), fill=(26, 25, 83), width=2)
#     profilePicture.line((i, 0, i, 400), fill=(100, 100, 100), width=5)
#     canvas.save("Profile_picture.png")
#     time.sleep(0.2)
#     # profilePicture.line((i + 1, 0, i + 1, 400), fill=(26, 25, 83), width=2)

profilePicture.rectangle((100, 120, 315, 315), fill="white", outline="black", width=7)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.rectangle((135, 135, 175, 200), fill=(0, 0, 0), width=5)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.rectangle((135, 170, 160, 200), fill=(100, 100, 110), width=5)
canvas.save("Profile_picture.png")
time.sleep(0.2)

profilePicture.rectangle((200, 135, 240, 200), fill=(0, 0, 0), width=5)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.rectangle((200, 170, 222, 200), fill=(100, 100, 110), width=5)
canvas.save("Profile_picture.png")
time.sleep(0.2)

profilePicture.rectangle((180, 250, 250, 290), fill=(0, 0, 0), width=5)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.rectangle((205, 275, 230, 290), fill=(125, 10, 15), width=5)
canvas.save("Profile_picture.png")
time.sleep(0.2)

for i in range(0, 40):
    profilePicture.line((60, 140 - i, 360, 140 - i), fill=(251, 192, 45), width=5)

canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.line((60, 105, 120, 105), fill=(231, 172, 25), width=10)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.line((60, 105, 60, 140), fill=(231, 172, 25), width=10)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.line((60, 140, 360, 140), fill=(231, 172, 25), width=10)
canvas.save("Profile_picture.png")
time.sleep(0.2)

for i in range(20, 120, 7):
    profilePicture.line(
        (85 + i, 140 - i, 335 - i, 140 - i), fill=(255, 143, 0), width=7
    )

canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.line((105, 120, 205, 20), fill=(235, 123, 0), width=7)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.line((105, 120, 315, 120), fill=(235, 123, 0), width=7)
canvas.save("Profile_picture.png")
time.sleep(0.2)

profilePicture.rectangle((65, 270, 135, 340), fill=(13, 71, 161), width=7)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.rectangle((45, 290, 155, 320), fill=(13, 71, 161), width=7)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.rectangle((85, 250, 115, 360), fill=(13, 71, 161), width=7)
canvas.save("Profile_picture.png")
time.sleep(0.2)
profilePicture.rectangle((85, 290, 115, 320), fill=(231, 172, 25), width=10)
canvas.save("Profile_picture.png")
time.sleep(0.2)


canvas.save("Profile_picture.png")
time.sleep(0.2)
