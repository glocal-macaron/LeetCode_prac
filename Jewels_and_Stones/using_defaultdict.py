class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq_dict = collections.defaultdict(int)

        for char in stones:
            freq_dict[char] += 1

        count = 0
        for char in jewels:
            count += freq_dict[char]
        
        return count