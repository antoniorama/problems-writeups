# Validate Binary Search Tree

## Problem Description

[LeetCode's 98](https://leetcode.com/problems/validate-binary-search-tree/description/)

## Solving the Problem

### O($n^2$) Time Complexity

This solution uses the raw definition of BST. So it checks the following:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees. (recursive)


```py
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        # check if all values of the left substree are less and if all values of the right subtree are greater
        if (root.left and not self.areAllLess(root, root.left)) or (root.right and not self.areAllGreater(root, root.right)):
            return False

        # recursively check the same for left and right subtrees
        return self.isValidBST(root.right) and self.isValidBST(root.left)
        
    def areAllGreater(self, original_root, root):
        # check if all are greater
        if not root:
            return True
        return root.val > original_root.val and self.areAllGreater(original_root, root.left) and self.areAllGreater(original_root, root.right)

    def areAllLess(self, original_root, root):
        # check if all are less
        if not root:
            return True
        return root.val < original_root.val and self.areAllLess(original_root, root.left) and self.areAllLess(original_root, root.right)
```

### O(n) Time Complexity

This is the desired solution, it runs DFS and creates min (left) and max (right) limits for the values that the nodes can have.

```py
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))
        
    def valid(self, node, left, right):
        if not node:
            return True

        if node.val <= left or node.val >= right:
            return False

        return self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right)
```