# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, Max):
            if not node:
                return 0
            count = 1 if node.val >= Max else 0
            Max = max(Max, node.val)
            count += dfs(node.left, Max)
            count += dfs(node.right, Max)
            return count
        return dfs(root, root.val)