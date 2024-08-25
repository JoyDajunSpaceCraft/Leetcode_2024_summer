# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        d = collections.deque()

        temp = head

        while temp.next:
            d.append(temp.next)
            temp = temp.next
        temp = head
        while d:
            temp.next =d.pop()
            temp = temp.next
            if len(d)>0:
                temp.next = d.popleft()
                temp = temp.next
        temp.next = None



        