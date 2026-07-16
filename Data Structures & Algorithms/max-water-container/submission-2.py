class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        l = 0
        r = len(h) - 1
        mA = 0
        while l < r:
            mB = min(h[l], h[r])
            cA = (r-l) * mB
            mA = max(cA, mA)
            if h[l] > h[r]:
                r-=1
            else:
                l+=1
        return mA

        