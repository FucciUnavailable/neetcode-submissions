class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        re = sorted(nums)
        counter = 1
        m = 1
        if len(nums) ==0:
            return 0
        for i in range(len(re)-1):
            
            s = re[i+1]
            c = re[i]
            if s==c:
                continue
            else:
                if s-c == 1:
                    counter += 1
                    m = max(counter,m)
                else:
                    counter = 1
        return m

            


            