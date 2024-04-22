# Daily Temperatures

## Problem Description

[LeetCode's 739](https://leetcode.com/problems/daily-temperatures)

## Solving the Problem

### O($n^2$) Time Complexity

We could use a brute-force approach that goes through the array and for each element checks the next elements until it finds a greater temperature.

```py
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize array
        nOfDays = [0] * len(temperatures)

        # main iteration
        for i in range(len(temperatures)):
            for k in range (i+1, len(temperatures)):
                if temperatures[k] > temperatures[i]:
                    nOfDays[i] = k - i
                    break

        return nOfDays
```

This solution has O(n) space complexity.

### O($n$) Time Complexity - Solution 1

Another solution would be having a lastDays array that keeps track of when a temperature occurred.

This array would have length 70 because temperatures go from 30 to 100 so the time complexity would be O(n), or technically O(70*n).

```py
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize arrays
        nOfDays = [0] * len(temperatures)
        lastDays = [-1 for _ in range(30, 101)]

        # main iteration
        for i in range(len(temperatures) - 1, -1, -1):
            # add to lastDays
            lastDays[temperatures[i] - 30] = i

            # add to nOfDays
            indexes = []
            for k in range(temperatures[i] - 29, 71):
                if lastDays[k] > i:
                    indexes.append(lastDays[k])
            
            if indexes:
                nOfDays[i] = min(indexes) - i

        return nOfDays
```

This solution is enought to pass all leetcode tests but with a high runtime.

### O(n) Time Complexity - Solution 2 (Stack)

A more sophisticated stack-based approach can optimize the problem further. By storing temperatures and their indices on a stack, it ensures that once a higher temperature is found, all previous lesser temperatures are resolved immediately.

This stack is a **Monotonic Decreasing Stack**

```py
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize data structures
        nOfDays = [0] * len(temperatures)
        stack = []

        # main iteration
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackIndex = stack.pop()[1]
                nOfDays[stackIndex] = i - stackIndex

            stack.append((temperatures[i], i))

        return nOfDays
```