class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for index, char in enumerate(s):
            # start가 뒤로 되돌아갈 우려가 있음 ex) abba
            if char in used and start <= used[char]: 
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[char] = index
        return max_length