class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq_dict = collections.Counter(stones)

        count = 0
        for char in jewels:
            count += freq_dict[char]
        return count