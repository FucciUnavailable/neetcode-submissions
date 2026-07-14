class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        nums = heights

        maxA = 0

        while l < r:
            minH = min(nums[l], nums[r])
            ar = (r-l) * minH
            maxA = max(maxA, ar)
            if nums[l] < nums[r]:
                l+=1
            else:
                r-=1
        return maxA