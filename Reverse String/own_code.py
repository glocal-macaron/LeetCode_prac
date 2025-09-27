class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front = 0
        back = len(s) - 1

        while front < back:
            # 이렇게 앞 뒤 동시 스왑이 가능함
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1