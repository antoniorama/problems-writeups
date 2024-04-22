import threading
import time

class ThreadCounter:

    def __init__(self, lock : bool) -> None:
        self.counter = 0
        self.lock = threading.Lock()
        
    def count(self, thread_no):
        while True:
            self.lock.acquire()
            self.counter += 1
            print(f"{thread_no}: Just increased counter to {self.counter}")
            time.sleep(1) # Equivalent to doing some work
            print(f"{thread_no}: Done some work. now value is {self.counter}")
            self.lock.release()
            time.sleep(1) # Some more work

userInput = str(input("Use locks? (Y/n) "))    
tc = ThreadCounter(False if userInput == "N" or userInput == "n" else True)

# 3 threads
for i in range(3):
    t = threading.Thread(target=tc.count, args=(i,))
    t.start()