import queue

q = queue.Queue()

for i in range(1, 11):
    q.put(i)

for i in range(1, 12):
    try:
        print(q.get(block=False))
    except queue.Empty:
        print("Finished")
