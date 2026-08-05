class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        s = []
        while r < len(nums) :
            sub = nums[l:r+1]

            s.append(max(sub))
            l+=1
            r+=1
        return s