class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, num in enumerate(nums):

            if i % 2 == 0:
                sum += num
        return sum