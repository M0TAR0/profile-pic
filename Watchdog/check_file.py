import os
import queue
import threading
import time
import random
from dotenv import load_dotenv
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

load_dotenv()

confirmation_q = queue.Queue()
test_path = os.getenv("TEST_DIRECTORY")
target_path = os.getenv("TARGET_DIRECTORY")


class myHandler(FileSystemEventHandler):
    def __init__(self, target_file):
        self.target = target_file

    def on_created(self, event):
        global confirmation_q
        if event.src_path == self.target:
            confirmation_q.put("Okay!")
            print("Veryfing...")
        else:
            print("That's not the correct file")


def error_function():
    global test_path
    global confirmation_q
    while confirmation_q.empty():
        error_time = random.randint(0, 6)
        time.sleep(error_time)
        error_number = random.randint(1001, 9999)
        p = Path(f"{test_path}error{error_number}")
        p.touch()


def create_key():
    global test_path
    creation_time = random.randint(5, 15)
    key = Path(f"{test_path}The_KEY.txt")

    time.sleep(creation_time)
    key.write_text("This is the one!")


# WATCHDOG
check_handler = myHandler(target_path)
checking_observer = Observer()
checking_observer.schedule(check_handler, path=test_path, recursive=False)  # type: ignore

# ERROR AND CREATION FUNCTION
error_thread = threading.Thread(target=error_function)
creation_thread = threading.Thread(target=create_key)

# MAIN LOOP
print("Loading...")
time.sleep(2)
print("Wait a moment...")
time.sleep(2)
print("\nWelcome! We will notify you when your file is ready.")

checking_observer.start()
creation_thread.start()
error_thread.start()

time.sleep(2)
while confirmation_q.empty():
    print("...")
    if not confirmation_q.empty():
        break
    time.sleep(2)

checking_observer.stop()
checking_observer.join()
error_thread.join()

for i in range(0, 7):
    print("\n")
print("\nYour file is ready!")
for i in range(0, 7):
    print("\n")
