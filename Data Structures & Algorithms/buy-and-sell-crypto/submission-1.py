class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        safe = prices[0]
        best = 0

        for i in range(len(prices)):
            safe = min(safe, prices[i])
            best = max(best, prices[i] - safe)
        return best