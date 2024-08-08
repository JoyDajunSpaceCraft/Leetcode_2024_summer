# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        path = []
        def backtrec(root):
            nonlocal res
            if not root: return 
            path.append(root.val)
            if root.left is None and root.right is None:
                res += get_sum(path)
            if root.left: 
                backtrec(root.left)
                path.pop()
            if root.right:
                backtrec(root.right)
                path.pop()
            
        
        def get_sum(path):
            s = 0
            for i in range(len(path)):
                s = s*10 + path[i]
            return s 
        backtrec(root)
        return res