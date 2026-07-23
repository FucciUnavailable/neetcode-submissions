class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        h = heights
        r = len(h) - 1
        maxA = 0
        while l < r:
            minB = min(h[l], h[r])
            curA = (r - l) * minB
            maxA = max(maxA, curA)
            if h[r] > h[l]:
                l+=1
            else:
                r-=1
        return maxA
