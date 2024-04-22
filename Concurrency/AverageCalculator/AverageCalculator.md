# Average Calculator - Concurrency

## Problem Statement

Given a stream of integer prices, we implemented a MovingAverage class which calculates the moving average of the last N prices.

```py
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.stream = []
        self.l = 0
        self.r = self.size -1
        self.count = 0

    def next(self, val: int) -> float:
        # 1. adds val price to the stream
        self.stream.append(val)

        # 2. returns the movign average of the last N prices
        if (len(self.stream) <= self.size):
            self.count += val
            return self.count / len(self.stream)

        self.count -= self.stream[self.l]
        self.l += 1
        self.r += 1
        self.count += self.stream[self.r]
        return self.count / self.size 
```

Now imagine that we have multiple external entities interacting with this class on the same object.

In this context, ensuring that the data structures are updated safely and effectively is essential.

## Solving the Problem

Let's dive into some questions and work on a solution while answering them.

### Describe a scenario where your implementation might fail in a multi-threaded environment

If thread A and thread B append values to the stream before thread A updates the count and the pointers, it could indeed lead to a significant problem. Here’s a breakdown of what could happen:

Example of this scenario:

Suppose the buffer size N is 3, and the stream initially contains [1, 2]. Here's how things might go wrong with threads A and B:

- Initial State: stream = [1, 2], self.count = 3, self.l = 0, self.r = 1
- Thread A appends 5: stream = [1, 2, 5]
- Thread B appends 10 before A updates count and pointers: stream = [1, 2, 5, 10]
- Thread A updates (assuming self.stream had only 1, 2, 5): self.count = 8, self.l = 1, self.r = 2
- Thread B updates based on the new stream (1, 2, 5, 10), but since it reads after A's append, it might adjust count and pointers incorrectly, assuming the wrong start or end positions or sum.

On AverageCalculator.py we can test different scenarios that go wrong . This file tests an implementation that launches 20 threads and doesn't have any Thread Safety mechanisms.

Some threads even have errors, like 'index out of range'.

Example of corrupted data:

```
Thread 0 added 4.
Thread 0 returning 4.0
Thread 1 added 9.
Thread 2 added 1.
Thread 1 returning 4.333333333333333
```

### How would you ensure thread safety in your implementation?

For ensuring that data is not changed by another thread, we should use Mutex Locks on sensible data.

I will be implementing this in AverageCalculatorLock.py , you can check the code in this file and also test that it solves the problem.

### What are the implications of using locks in your solution? How might they affect performance?

While locks protect against data inconsistency and potential errors due to concurrent modifications, they can significantly **slow down the system** by limiting the effective parallelism and increasing waiting times due to thread blocking.

### Could you use any lock-free techniques to implement the MovingAverage class?

### What changes would you make to your design if updates and queries come in at a very high rate?
