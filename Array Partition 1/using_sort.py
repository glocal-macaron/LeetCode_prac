class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        pair = list()

        for num in nums:
            
            pair.append(num)

            if len(pair) == 2:
                sum += min(pair[0], pair[1])
                pair = []
        return sum
            