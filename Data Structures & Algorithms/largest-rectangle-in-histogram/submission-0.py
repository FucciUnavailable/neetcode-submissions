class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stk = [] # pair: (index,height)

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                idx, hgt = stk.pop()
                maxArea = max(maxArea, hgt * (i- idx))
                start = idx
            stk.append((start,h))
        for i,h in stk:
            maxArea = max(maxArea, h *(len(heights) - i))
        return maxArea 