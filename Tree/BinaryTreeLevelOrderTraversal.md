# Binary Tree Level Order Traversal

## Problem Description

[LeetCode's 102](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

## Solving the Problem



### DFS - Stack


```py
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1, leafs2 = [], []

        # Perform DFS on tree 1
        stack1 = [root1]

        while stack1:
            node = stack1.pop()

            if node.right:
                stack1.append(node.right)
            if node.left:
                stack1.append(node.left)

            # leaf found
            if not node.right and not node.left:
                leafs1.append(node.val)

        # Perform DFS on tree 2
        stack2 = [root2]

        while stack2:
            node = stack2.pop()

            if node.right:
                stack2.append(node.right)
            if node.left:
                stack2.append(node.left)

            # leaf found
            if not node.right and not node.left:
                leafs2.append(node.val)

        return leafs1 == leafs2
```

### DFS - Recursive

```py
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1, leafs2 = [], []

        def dfs(root, leafsList):
            if not root.left and not root.right:
                leafsList.append(root.val)
            else:
                if root.left:
                    dfs(root.left, leafsList)
                if root.right:
                    dfs(root.right, leafsList)


        dfs(root1, leafs1)
        dfs(root2, leafs2)

        return leafs1 == leafs2
```