# Simple Counter

## Introduction

This is a trivial non-real world example to understand the concept of Locks / Mutex Locks.

## Problem Description

Imagine a system where multiple entities, each operating in its own thread, are updating the same piece of data. This scenario often leads to a common problem in multi-threaded environments known as a "race condition," where the output and the state of the shared data depend on the sequence and timing of threads' execution.

In this example, we consider a simple shared counter (an integer variable) being incremented by multiple threads:
```py
class ThreadCounter:

    def __init__(self) -> None:
        self.counter = 0
        
    def count(self, thread_no):
        while True:
            self.counter += 1
            print(f"{thread_no}: Just increased counter to {self.counter}")
            time.sleep(1) # Equivalent to doing some work
            print(f"{thread_no}: Done some work. now value is {self.counter}")
            time.sleep(1) # Some more work
```

How do we make sure that the data is not modified by another thread during the 'doing some work' time?

This problem is inspired in this [video](https://www.youtube.com/watch?v=MbFSuk8yyjY)
## Solving the Problem

Let's use the threading python library to test this scenario in practice.

```py
import threading
```

We'll create multiple threads to manipulate the counter concurrently:


```py
tc = ThreadCounter()

# 3 threads
for i in range(30):
    t = threading.Thread(target=tc.count, args=(i,))
    t.start()
```

If we run this code. We can see that the counter value is affected by other threads:

```
0: Just increased counter to 1
1: Just increased counter to 2
2: Just increased counter to 3
0: Done some work. now value is 3
1: Done some work. now value is 3
```

We can solve this by using a Mutex Lock:

```py
class ThreadCounter:

    def __init__(self) -> None:
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
```

This works like this: 

- A thread takes the lock and says 'I acquire the lock' until they release it. 

- If a thread attempts to acquire the lock but it's already held, the thread will block (wait) until the lock becomes available.

- This ensures only one thread can work at the locked section at a specific time frame.

We can observe the result:

```
0: Just increased counter to 1
0: Done some work. now value is 1
1: Just increased counter to 2
1: Done some work. now value is 2
2: Just increased counter to 3
2: Done some work. now value is 3
0: Just increased counter to 4
0: Done some work. now value is 4
1: Just increased counter to 5
1: Done some work. now value is 5
```