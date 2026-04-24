class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rA = [1] * len(nums)
        lA = [1] * len(nums)
        rs =1 
        ls = 1
        r = len(nums) - 1
        l = 0
        res = [1] * len(nums)
        while r > 0:
            rs *= nums[r]
            ls *= nums[l]
            rA[r] = rs
            lA[l] = ls
            r -=1
            l+=1
        print(rA)
        print(lA)
        for i in range(len(nums)):
            prev = 1
            post = 1
            try:
                prev = lA[i-1]
                post = rA[i+1]
                
            except:
                pass
            res[i] = post * prev
        return res

        
            