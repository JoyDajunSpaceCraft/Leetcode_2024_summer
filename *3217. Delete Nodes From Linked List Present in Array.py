# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # nums_set = set(nums)
        # dummy = ListNode(0)
        # dummy.next = head

        # current = dummy
        # while current and current.next:
        #     if current.next.val in nums:
        #         current.next = current.next.next
        #     else:
        #         current = current.next
        # return dummy.next
        # 使用 set 存储 nums 中的值，以加快查找速度
        nums_set = set(nums)
        
        # 哨兵节点，指向链表头
        dummy = ListNode(0)
        dummy.next = head
        
        # 当前节点的指针
        current = dummy
        
        # 遍历链表
        while current and current.next:
            if current.next.val in nums_set:
                # 跳过当前节点的下一个节点
                current.next = current.next.next
            else:
                # 保留当前节点
                current = current.next
        
        # 返回哨兵节点的下一个节点，即新的链表头
        return dummy.next