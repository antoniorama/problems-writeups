# Linked List Cycle

## Problem Description

[LeetCode's 141](https://leetcode.com/problems/linked-list-cycle/description)

## Solving the Problem

### O(n) Space Complexity

This problem can be solved by keeping track of the already visited nodes (pointers to these nodes) in a **HashSet**.

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()

        while head:
            if head in hashSet:
                return True

            hashSet.add(head)
            head = head.next

        return False
```

### O(1) Space Complexity

This algorithm is not necessarily intuitive and might not be easy to derive without prior knowledge or specific insight into this class of problems. It is uniquely suited for detecting cycles in linked lists.

An optimal way to detect a cycle in a linked list without additional memory is by using the Floyd's Tortoise and Hare algorithm. This method involves two pointers, often called **slow and fast pointers**. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle in the list, the fast pointer will eventually meet the slow pointer, proving the existence of a cycle.

```py
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True

        return False
```

## Follow-up Questions

- How would you find the starting point of the cycle?

[LeetCode's 142](https://leetcode.com/problems/linked-list-cycle-ii/)