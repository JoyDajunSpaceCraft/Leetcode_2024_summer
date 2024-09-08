# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        
        length = 0
        current = head
        while current:
            length +=1
            current = current.next
        
        res = []
        part_size = length//k
        reminder=length %k
        current = head
        for i in range(k):
            part_head = current
            part_len = part_size + (1 if i < reminder else 0)
            for j in range(part_len-1):
                if current:
                    current = current.next
            
            if current:    
                next_head = current.next
                current.next = None
                current = next_head
            res.append(part_head)
        return res


        