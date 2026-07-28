class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        n = numbers
        r = len(n) - 1
        t = target
        while l < r:
            s = n[l] + n[r]
            if s == t:
                return [l+1,r +1]
            elif s > t:
                r -=1
            else:
                l+=1
        return []