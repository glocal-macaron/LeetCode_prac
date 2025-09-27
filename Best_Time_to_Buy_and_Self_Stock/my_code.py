class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_merit = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                max_merit = max(prices[j] - prices[i], max_merit)
        return max_merit
