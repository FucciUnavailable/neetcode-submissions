class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        t = 0
        cntr = 1
        if len(ss) == 0:
            return 0
        for n in ss:
            if n-1 not in ss:
                st = n
                while st + 1 in ss:
                    cntr +=1
                    st +=1
                t=  max(t,cntr)
                cntr = 1
        return t            
            


            