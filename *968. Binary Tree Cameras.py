# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = [0]
        if self.traversal(root, result) == 0:
            result[0] +=1
        return result[0] 

    def traversal(self, cur:TreeNode, result: List[int]) -> int:
        if not cur:
            return 2
        left = self.traversal(cur.left, result)
        right = self.traversal(cur.right, result)

        if left ==2 and right == 2:
            return 0
        elif left ==0 or right==0:
            result[0]+=1
        else:
            return 2
