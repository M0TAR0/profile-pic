from PIL import Image, ImageDraw

canvas = Image.new("RGB", (500, 500), "white")

drawing = ImageDraw.Draw(canvas)

# drawing.circle((250, 250), radius=50, fill="black")
# drawing.line((250, 200, 250, 0), fill="black", width=10)
# drawing.line((300, 250, 500, 250), fill="black", width=10)
# drawing.line((250, 300, 250, 500), fill="black", width=10)
# drawing.line((200, 250, 0, 250), fill="black", width=10)
# canvas.show()
# canvas.save("drawing3_circle.jpg")

#  ELLIPSES

# drawing.ellipse((0, 0, 500, 100), fill="black", outline="red")
# drawing.ellipse((100, 100, 400, 200), fill=(255, 238, 199), outline="yellow")
# drawing.ellipse((200, 200, 300, 300), fill=(241, 153, 43), outline="blue")
# drawing.ellipse((225, 300, 275, 400), fill=(173, 23, 238), outline="purple")
# drawing.ellipse((245, 400, 255, 500), fill=(127, 32, 98), outline="green")
# canvas.show()
# canvas.save("drawing4_ellipses.jpg")

# ARCS, PIESLICES AND CHORDS

for i in range(0, 500, 100):
    drawing.arc((i, 0, i + 100, 100), 0, 90, fill="black", width=3)

for i in range(0, 500, 100):
    drawing.arc((i, 100, i + 100, 200), 0, 90, fill="black", width=3)
    drawing.line((i + 50, 200, i, 200), fill="black", width=3)

for i in range(0, 500, 100):
    drawing.pieslice((i, 200, i + 100, 300), 0, 90, fill="black", width=3)
    drawing.line((i + 50, 300, i, 300), fill="black", width=3)

for i in range(0, 500, 100):
    drawing.chord((i, 300, i + 100, 400), 0, 180, fill="black", width=3)
    drawing.line((i + 50, 400, i, 400), fill="black", width=3)

canvas.show()
canvas.save("Drawing5_circlethings.jpg")
