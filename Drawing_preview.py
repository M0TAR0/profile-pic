import os
import queue
import tkinter
import subprocess
from dotenv import load_dotenv
from PIL import Image, ImageTk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

load_dotenv()

# FILE PATHS
drawingScript = os.getenv("DRAWING_SCRIPT")
drawingDirectory = os.getenv("DRAWING_DIRECTORY")
drawingFile = os.getenv("DRAWING_FILE")
drawingScriptDirectory = os.getenv("DRAWING_SCRIPT_PATH")


# QUEUE
drawingQueue = queue.Queue()


# WATCHDOG HANDLER
class DrawingChangeHandler(FileSystemEventHandler):
    def __init__(self, drawingScript):
        self.drawingScript = drawingScript

    def on_created(self, event):
        if event.src_path == self.drawingScript:
            drawingQueue.put("CHANGE")
            print("Event created:", event.src_path)

        #   def on_modified(self, event):
        # if event.src_path == self.drawingScript:
        #   drawingQueue.put("CHANGE")
        #    print("Event modified:", event.src_path)


# WATCHDOG THREAD
changeHandler = DrawingChangeHandler(drawingScript)
changeObserver = Observer()
changeObserver.schedule(changeHandler, path=drawingScriptDirectory, recursive=False)  # type: ignore
changeObserver.start()


# TK CHANGES MONITOR
def change_monitor():
    global tkdrawingPicture
    try:
        drawingQueue.get(block=False)
        subprocess.run(["python", f"{drawingScript}"])

        drawingPicture = Image.open(drawingFile)  # type: ignore
        tkdrawingPicture = ImageTk.PhotoImage(drawingPicture)
        drawing.config(image=tkdrawingPicture)

    except queue.Empty:
        pass

    root.after(100, change_monitor)


# TKINTER SETUP
root = tkinter.Tk()
root.geometry("1000x1000")

mainframe = tkinter.Frame(root, pady=20)
mainframe.pack()

drawingPicture = Image.open(drawingFile)  # type: ignore
tkdrawingPicture = ImageTk.PhotoImage(drawingPicture)
drawing = tkinter.Label(mainframe, image=tkdrawingPicture)
drawing.pack()

root.after(500, change_monitor)
root.mainloop()
