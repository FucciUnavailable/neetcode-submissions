class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        res= []
        for i in range(len(nums) -2):
            if i > 0 and n[i] == n[i -1]:
                continue
            l = i+1
            r = len(n) - 1

            while l < r :
                s = n[i] + n[r] + n[l]
                if s == 0:
                    res.append([n[i] , n[r] ,n[l]])
                    l+=1
                    r-=1
                    while l < r and n[l] == n[l-1]:
                        l+=1
                    while l<r and n[r] == n[r+1]:
                        r-=1
                elif s < 0:
                    l+=1
                else:
                    r-=1
        return res
