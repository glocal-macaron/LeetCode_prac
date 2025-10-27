class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq_dict = {}

        for char in stones:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
        
        count = 0
        for char in jewels:
            if char in freq_dict:
                count += freq_dict[char]
        return count