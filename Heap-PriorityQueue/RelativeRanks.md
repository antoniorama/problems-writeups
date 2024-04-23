# Relative Ranks

## Problem Description

[LeetCode's 506](https://leetcode.com/problems/relative-ranks/description/)

## Solving the Problem

### O($n^2$) Time Complexity

This problem can be solved by sorting the array ( O(nlogn) ), and then, for each element of the original array, check the sorted array for the position (index + 1).
```py
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        output = []

        sortedScores = sorted(score, reverse=True)

        for s in score:
            for i in range(len(sortedScores)):
                if s == sortedScores[i]:
                    if i == 0:
                        output.append("Gold Medal")
                    elif i == 1:
                        output.append("Silver Medal")
                    elif i == 2:
                        output.append("Bronze Medal")
                    else:
                        output.append(str(i+2))

        return output
```

The space complexity of this solution is O(n)

### O(nlogn) Time Complexity - HashMap

A better version of the previous solution can be obtained by storing the elements and their indexes in a HashMap after sorting the array. 

```py
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        output = []

        sortedScores = sorted(score, reverse=True)

        hashMap = {}
        for i in range(len(sortedScores)):
            if i == 0:
                hashMap[sortedScores[i]] = "Gold Medal"
            elif i == 1:
                hashMap[sortedScores[i]] = "Silver Medal"
            elif i == 2:
                hashMap[sortedScores[i]] = "Bronze Medal"
            else:
                hashMap[sortedScores[i]] = str(i+1)

        for s in score:
            output.append(hashMap[s])

        return output
```

### O(nlogn) Time Complexity - MaxHeap

This problem can also be solved with a MaxHeap approach where we start by constructing a MaxHeap with (score, i) elements from the score array.

Note that we're using Python's ```heapq``` module and it will consider the first element of the tuple to be the value by which to order the heap.

Afterwards, we pop from the heap and update the output array accordingly.

```py
from heapq import heappush, heappop

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Construct the heap
        maxHeap = []
        for i in range(len(score)):
            heappush(maxHeap, (-score[i], i))

        output = [None for _ in range(len(score))]

        # Iterate maxHeap and update output
        curr = 0
        while maxHeap:
            _, i = heappop(maxHeap)

            if curr == 0:
                output[i] = "Gold Medal"
            elif curr == 1:
                output[i] = "Silver Medal"
            elif curr == 2:
                output[i] = "Bronze Medal"
            else:
                output[i] = str(curr+1)

            curr += 1

        return output
```

This solution performs slightly better but the time complexity is still O(n).

The space complexity is O(n) due to the maxHeap.

## Follow-up Questions

- Handling Real-time Scores

Build a class that handles scores coming in real time.

(TODO)