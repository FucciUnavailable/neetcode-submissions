class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for j in range(len(nums)):
            no = j
            s = 1
            for i in range(len(nums)):
                if i != no:
                    s *= nums[i]
            res[no] = s
        return res
    

