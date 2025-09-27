# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         addList = ListNode()
#         origin: ListNode = addList
#         carry = 0

#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0
#             total = v1 + v2 + carry
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
#             sum = total % 10


#             addList.val = sum
#             carry = total // 10
#             if carry or l1 or l2:
#                 addList.next = ListNode()
#                 addList = addList.next

#         return origin


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        origin = addList = ListNode()
        carry = 0

        while l1 or l2 or carry:
            sum  = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            addList.next = ListNode(val)
            addList = addList.next

        return origin.next