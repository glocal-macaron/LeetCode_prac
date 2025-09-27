class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = list()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        # 문자 리스트의 개수를 먼저 생각함.
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True