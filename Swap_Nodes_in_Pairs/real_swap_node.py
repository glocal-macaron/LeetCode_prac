# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # head 이전 연결 리스트가 필요하기에 prev 사용
        root = prev = ListNode()

        prev.next = head

        while head and head.next:

            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        # prev를 더미로 만들었기 때문에 더미 다음 노드를 반환
        return root.next
