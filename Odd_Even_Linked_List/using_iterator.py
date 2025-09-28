# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = even_head = head.next

        # 짝수를 조건으로 하는 이유
        # odd.next와 even.next가 존재 해야 하는데 odd로 조건을 만들면 리스트 노드 개수가 짝수일 때, odd.next는 존재하는데 even.next는 존재하지 않을 수 있음
        # 그래서 even.next가 존재할 때 odd.next는 무조건 존재하기 때문에 even을 조건으로 사용
        while even and even.next:
            # odd.next는 객체 주소를 저장하는 "공간"
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head

        return head
        