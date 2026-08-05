class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        safe = prices[0]

        p = prices

        for i in range(len(prices)):
            safe = min(safe, p[i])
            best = max(best, p[i] - safe)
        return best
        