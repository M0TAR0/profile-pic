import threading
import time

start_time = time.perf_counter()

counter = 0
counter2 = 0
lock = threading.Lock()


def count():
    global counter
    global counter2
    for i in range(0, 1000000):
        counter2 += 1
        with lock:
            counter += 1


t = threading.Thread(target=count)
t2 = threading.Thread(target=count)

t.start()
t2.start()

first_stop = time.perf_counter()
first_time = first_stop - start_time

print(counter)
print(counter2)
print("First Time:", first_time)

t.join()
t2.join()

print(counter)
print(counter2)
final_end_time = time.perf_counter()
end_time = final_end_time - start_time
print("Final end time:", end_time)
