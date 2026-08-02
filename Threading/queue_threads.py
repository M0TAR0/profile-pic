import threading
import queue
import time

message_list = queue.Queue()


def place(wait_time, message):
    global message_list
    print("Hold on, please wait:", wait_time, "seconds")
    time.sleep(wait_time)
    message_list.put(message)


def check_if_message(wait_time):
    message = ""

    time.sleep(wait_time)
    print("Checking for your message...")
    while message_list.empty():
        print("Sorry... we are waiting for your file.")
        time.sleep(2)
    message = message_list.get()
    print("Done!")
    time.sleep(2)
    print("Wait...")
    time.sleep(2)
    print("Your message is: ", message)


t1 = threading.Thread(target=place, args=(10, "Hello World!"))
t2 = threading.Thread(target=check_if_message, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Thanks for using this!")
