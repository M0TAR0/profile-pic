import time
from watchdog import events
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv
import os

load_dotenv()


class myHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("You just created:", event.src_path)


creation_handler = myHandler()
creation_observer = Observer()
creation_observer.schedule(
    creation_handler, path=os.getenv("TEST_DIRECTORY"), recursive=False
)  # type: ignore
creation_observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    creation_observer.stop()

creation_observer.join()

print("\nYOU FINISHED THE OBSERVATION!")
