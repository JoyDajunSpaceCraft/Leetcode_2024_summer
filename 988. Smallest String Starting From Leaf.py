# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.smallest = '~'
        def dfs(node, path):
            if node:
                path = chr(node.val + ord('a')) + path
                if not node.left and not node.right:
                    if path < self.smallest:
                        self.smallest = path
                dfs(node.left, path)
                dfs(node.right, path)
        dfs(root, "")
        return self.smallest

