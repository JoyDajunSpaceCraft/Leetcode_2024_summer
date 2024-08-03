"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traversal(cur:'Node')-> 'Node':
            if not cur: return []
            if cur.left: cur.left.next = cur.right
            if cur.right:
                if cur.next:
                    cur.right.next = cur.next.left
                else:
                    cur.right.next =None
            traversal(cur.left)
            traversal(cur.right)
        traversal(root)
        return root