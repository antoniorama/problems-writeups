import threading
import random

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.stream = []
        self.l = 0
        self.r = self.size -1
        self.count = 0

    def next(self, threadNo, val: int) -> float:
        # 1. adds val price to the stream
        self.stream.append(val)
        print_output(f"Thread {threadNo} added {val}.")

        # 2. returns the moving average of the last N prices
        if (len(self.stream) <= self.size):
            self.count += val
            result = self.count / len(self.stream)
            print_output(f"Thread {threadNo} returning {result}")
            return result

        self.count -= self.stream[self.l]
        self.l += 1
        self.r += 1
        self.count += self.stream[self.r]
        result = self.count / self.size
        print_output(f"Thread {threadNo} returning {result}")
        return result

# Output lock to ensure messages don't get mixed up
output_lock = threading.Lock()

def print_output(message):
    with output_lock:
        print(message)

mA = MovingAverage(3)
threads = []

# Creating 20 threads
for i in range(20):
    val = random.randint(0, 10)
    t = threading.Thread(target=mA.next, args=(i, val,))
    threads.append(t)
    t.start()

# Ensuring all threads have completed
for t in threads:
    t.join()
