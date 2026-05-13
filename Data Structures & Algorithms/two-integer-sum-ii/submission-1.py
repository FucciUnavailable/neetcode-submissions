class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        n = numbers
        r = len(n) - 1
        t = target
        while l < r:
            s = n[l] + n[r]
            if s > t:
                r -=1
            elif s<t:
                l+=1
            else:
                return[l+1,r+1]
        return[l,r] 
