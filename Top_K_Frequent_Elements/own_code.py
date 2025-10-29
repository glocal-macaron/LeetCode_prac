class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        higher = []

        flag = 1
        for key, value in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            if flag <= k:
                higher.append(key)
            flag += 1
        

        return higher