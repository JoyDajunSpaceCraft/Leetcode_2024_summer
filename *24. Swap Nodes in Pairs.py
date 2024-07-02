# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumphead = ListNode(next = head)
        cur = dumphead

        while cur.next and cur.next.next:
            temp = cur.next
            temp1 = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = temp
            temp.next = temp1
            cur = cur.next.next
        return dumphead.next