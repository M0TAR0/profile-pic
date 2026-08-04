import os
import time
from PIL import Image
from PIL import ImageDraw
from dotenv import load_dotenv

load_dotenv()

drawingFile = os.getenv("DRAWING_FILE")
draw = Image.new("RGB", (736, 981), (255, 255, 255))
draw.save(drawingFile)  # type: ignore
time.sleep(5)

# COLORS
colors = {
    "black": {"fill": "black", "width": 5},
    "yellow": {"fill": "yellow", "width": 5},
    "green": {"fill": "green", "width": 5},
    "yellow_poo": {"fill": (253, 195, 61), "width": 10, "outline": "black"},
}

# INSTRUCTIONS
operations = [
    ("rectangle", (130, 20, 170, 35), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (570, 20, 610, 35), {"fill": (253, 195, 61)}),  # Body
    #
    ("rectangle", (100, 35, 200, 50), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (540, 35, 635, 50), {"fill": (253, 195, 61)}),  # Body
    #
    ("rectangle", (87, 50, 210, 120), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (527, 50, 650, 120), {"fill": (253, 195, 61)}),  # Body
    #
    ("rectangle", (105, 120, 195, 140), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (545, 120, 635, 140), {"fill": (253, 195, 61)}),  # Body
    #
    ("rectangle", (305, 10, 440, 23), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (260, 23, 490, 36), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (225, 36, 525, 50), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (200, 50, 550, 65), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (150, 65, 600, 140), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (115, 140, 635, 200), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (115, 200, 635, 265), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (130, 265, 620, 280), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (118, 280, 647, 300), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (99, 300, 667, 325), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (83, 325, 680, 417), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (100, 417, 670, 435), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (110, 435, 655, 450), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (127, 450, 636, 470), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (150, 470, 610, 500), {"fill": (253, 195, 61)}),  # Body
    #
    ("rectangle", (135, 490, 620, 500), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (125, 500, 635, 510), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (105, 510, 657, 525), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (86, 525, 673, 540), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (72, 540, 688, 555), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (60, 555, 700, 570), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (52, 570, 710, 585), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (52, 585, 700, 600), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (58, 600, 702, 615), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (54, 615, 705, 630), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (54, 630, 705, 650), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (52, 650, 705, 670), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (65, 650, 695, 690), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (75, 650, 685, 700), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (127, 650, 630, 750), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (152, 750, 607, 760), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (127, 740, 625, 770), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (133, 770, 625, 790), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (145, 790, 615, 820), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (158, 820, 603, 850), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (175, 850, 585, 870), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (190, 870, 570, 890), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (208, 890, 552, 900), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (220, 890, 360, 915), {"fill": (253, 195, 61)}),  # Body
    ("rectangle", (390, 890, 545, 915), {"fill": (253, 195, 61)}),  # Body
    # Space
    ("rectangle", (135, 490, 180, 500), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (580, 490, 620, 500), {"fill": (233, 24, 55)}),  # shirt
    #
    ("rectangle", (125, 500, 200, 510), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (555, 500, 635, 510), {"fill": (233, 24, 55)}),  # shirt
    #
    ("rectangle", (105, 510, 245, 525), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (521, 510, 657, 525), {"fill": (233, 24, 55)}),  # shirt
    #
    ("rectangle", (86, 525, 275, 540), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (475, 525, 673, 540), {"fill": (233, 24, 55)}),  # shirt
    #
    ("rectangle", (72, 540, 290, 555), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (460, 540, 688, 555), {"fill": (233, 24, 55)}),  # shirt
    #
    ("rectangle", (60, 555, 312, 570), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (435, 555, 700, 570), {"fill": (233, 24, 55)}),  # shirt
    #
    ("rectangle", (52, 570, 710, 585), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (84, 585, 659, 600), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (105, 600, 638, 615), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (117, 615, 620, 630), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (129, 630, 623, 650), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (127, 650, 630, 750), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (152, 750, 607, 760), {"fill": (233, 24, 55)}),  # shirt
    ("rectangle", (202, 760, 557, 770), {"fill": (233, 24, 55)}),  # shirt
    (
        "arc",  # Left Ear
        (80, 20, 220, 150),
        {"start": 115, "end": 325, "fill": (0, 0, 0), "width": 10},
    ),
    (
        "arc",  # Right Ear
        (520, 20, 660, 150),
        {"start": 210, "end": 60, "fill": "black", "width": 10},
    ),
    (
        "arc",  # Upper Head
        (105, 5, 645, 400),
        {"start": 155, "end": 382, "fill": "black", "width": 10},
    ),
    (
        "arc",  # bottom head
        (75, 200, 690, 540),
        {"start": 323, "end": 215, "fill": "black", "width": 10},
    ),
    (
        "arc",  # Neck
        (270, 450, 480, 580),
        {
            "start": 10,
            "end": 170,
            "width": 10,
            "fill": "black",
        },
    ),
    (
        "arc",  # Left Shoulder
        (40, 434, 720, 802),
        {"start": 190, "end": 230, "fill": "black", "width": 12},
    ),
    (
        "arc",  # Right Shoulder
        (40, 434, 720, 802),
        {"start": 312, "end": 350, "fill": "black", "width": 12},
    ),
    (
        "arc",  # Left Sleeve
        (-100, 574, 145, 780),
        {"start": 285, "end": 340, "fill": "black", "width": 12},
    ),
    (
        "arc",  # Right sleeve
        (600, 578, 800, 780),
        {"start": 215, "end": 277, "fill": "black", "width": 12},
    ),
    (
        "arc",  # hand
        (45, 550, 170, 710),
        {
            "start": 70,
            "end": 215,
            "width": 10,
            "fill": "black",
        },
    ),
    (
        "arc",  # hand
        (590, 550, 715, 710),
        {
            "start": 320,
            "end": 110,
            "width": 10,
            "fill": "black",
        },
    ),
    (
        "arc",
        (120, 450, 640, 970),
        {"start": 125, "end": 210, "fill": "black", "width": 10},  # legs
    ),
    ("line", (232, 916, 359, 916), {"fill": "black", "width": 10}),  # left lef
    (
        "arc",
        (120, 450, 640, 970),
        {"start": 330, "end": 415, "fill": "black", "width": 10},  # Right lef
    ),
    ("line", (395, 916, 530, 916), {"fill": "black", "width": 10}),  # Right leg
    (
        "arc",
        (250, 750, 385, 950),
        {"start": 20, "end": 46, "fill": "black", "width": 15},  # lef leg
    ),
    (
        "arc",
        (362, 750, 580, 950),
        {"start": 135, "end": 180, "fill": "black", "width": 10},  # right leg
    ),
    (
        "arc",
        (300, 800, 440, 850),
        {"start": 0, "end": 180, "fill": "black", "width": 10},  # between legs
    ),
    (
        "arc",  # Tummy line
        (122, 700, 635, 780),
        {"start": 0, "end": 180, "fill": "black", "width": 10},
    ),
    (
        "arc",  # Eyebrows
        (180, 120, 370, 300),
        {"start": 200, "end": 270, "fill": "black", "width": 12},
    ),
    (
        "arc",
        (380, 120, 560, 300),
        {"start": 260, "end": 330, "fill": "black", "width": 12},
    ),
    (
        "circle",  # Eyes
        (270, 330),
        {"radius": 25, "fill": "black"},
    ),
    (
        "circle",
        (475, 330),
        {"radius": 25, "fill": "black"},
    ),
    (
        "circle",  # inner Eyes
        (263, 325),
        {"radius": 7, "fill": "white"},
    ),
    (
        "circle",  # inner Eyes
        (468, 325),
        {"radius": 7, "fill": "white"},
    ),
    (
        "chord",
        (340, 325, 400, 373),
        {"start": 0, "end": 360, "fill": "black", "width": 10},
    ),
    (
        "arc",  # smile
        (320, 410, 420, 460),
        {"start": 0, "end": 160, "fill": "black", "width": 13},
    ),
]

drawing = ImageDraw.Draw(draw)
for i, (shape, coords, kwargs) in enumerate(operations):
    stroke = getattr(drawing, shape)
    stroke(coords, **kwargs)
    time.sleep(0.1)
    draw.save(drawingFile)  # type: ignore
