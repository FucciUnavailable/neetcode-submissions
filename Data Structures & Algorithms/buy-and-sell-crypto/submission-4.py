class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        store = 0
        p = prices
        for r in range(len(prices)):
            if p[r] < p[l]:
                l = r
            store = max(store, p[r] - p[l])
        return store