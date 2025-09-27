class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list()
        init = 1

        for i in range(len(nums)):
            result.append(init)
            init = init * nums[i]
    # nums: [1, 2, 3, 4]
    # result: [1, 1, 2, 6] = [init, init * 1, init * 1 * 2, init * 1 * 2 * 3]

        init = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * init
            init = init * nums[i]
    # nums: [1, 2, 3, 4]
    # result: [1, 1, 2, 6] = [init * 4, init * 4 * 3, init * 4 * 3 * 2, init * 4 * 3 * 2 * 1]

        return result