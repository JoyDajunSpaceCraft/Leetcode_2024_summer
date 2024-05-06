# https://leetcode.com/problems/remove-nodes-from-linked-list/description/?envType=daily-question&envId=2024-05-06
# Solution: https://leetcode.com/problems/remove-nodes-from-linked-list/solutions/5118366/detailed-explanation-3-approaches-stack-recursion-reversal-o-1-space-efficient !!!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        
        nxt = None
        while stack: # [13, 8]

            cur = stack.pop() #stack= [13] cur = [8]
            cur.next = nxt # cur
            nxt = cur
        return cur 