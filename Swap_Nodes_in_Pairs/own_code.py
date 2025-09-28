# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        root = head

        # 조건 GPT 도움 받음
        # head.next만 있으면 head가 None 일 때 문제가 생김
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next

        return root
