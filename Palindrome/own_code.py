class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = list()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        flag = True
        for i in range(len(strs)):
            back = len(strs) - 1 - i
            front = i
            if back <= front:
                break
            else:
                if strs[front] == strs[back]:
                    continue
                else:
                    flag = False
                    break
        return flag