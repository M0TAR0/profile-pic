import os
import queue
import tkinter
from dotenv import load_dotenv
from PIL import Image, ImageTk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

load_dotenv()

# FILE PATHS
drawingScript = os.getenv("DRAWING_SCRIPT")
drawingDirectory = os.getenv("DRAWING_SCRIPT_PATH")
drawingFile = os.getenv("DRAWING_FILE")
drawingScriptDirectory = os.getenv("DRAWING_SCRIPT_PATH")


# QUEUE
drawingQueue = queue.Queue()


# WATCHDOG HANDLER
class DrawingChangeHandler(FileSystemEventHandler):
    def __init__(self, drawingFile):
        self.drawingFile = drawingFile

    def on_created(self, event):
        if event.src_path == self.drawingFile:
            drawingPicture = Image.open(self.drawingFile)  # type: ignore
            drawingQueue.put(drawingPicture)
            print("Event created:", event.src_path)

    def on_modified(self, event):
        if event.src_path == self.drawingFile:
            drawingQueue.put("It changed")
            print("Event modified:", event.src_path)


# WATCHDOG THREAD
changeHandler = DrawingChangeHandler(drawingFile)
changeObserver = Observer()
changeObserver.schedule(changeHandler, path=drawingDirectory, recursive=False)  # type: ignore
changeObserver.start()


# TK CHANGES MONITOR
def change_monitor():
    global tkdrawingPicture
    try:
        drawingQueue.get(block=False)
        try:
            drawingPicture = Image.open(drawingFile)  # type: ignore
            drawingPicture.load()
        except (IOError, Image.UnidentifiedImageError):
            root.after(100, change_monitor)
            return

        tkdrawingPicture = ImageTk.PhotoImage(drawingPicture)
        drawing.config(image=tkdrawingPicture)

    except queue.Empty:
        pass

    root.after(100, change_monitor)


# TKINTER SETUP
root = tkinter.Tk()
root.title("Drawing Window")
root.geometry("1000x1000")

mainframe = tkinter.Frame(root, pady=20)
mainframe.pack()

drawingPicture = Image.open(drawingFile)  # type: ignore
tkdrawingPicture = ImageTk.PhotoImage(drawingPicture)
drawing = tkinter.Label(mainframe, image=tkdrawingPicture)
drawing.pack()

root.after(50, change_monitor)
root.mainloop()
