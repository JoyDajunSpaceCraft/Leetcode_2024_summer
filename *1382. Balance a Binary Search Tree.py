# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []

        def traversal(cur:TreeNode):
            if not cur: return 
            traversal(cur.left)
            res.append(cur.val)
            traversal(cur.right)
        def getTree(nums, left, right):
            if left>right:return 
            mid = left +(right-left)//2
            root = TreeNode(nums[mid])
            root.left = getTree(nums, left, mid-1)
            root.right = getTree(nums, mid+1, right)
            return root
        traversal(root)
        print(res)
        return getTree(res, 0, len(res)-1)