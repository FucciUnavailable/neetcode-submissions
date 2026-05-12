class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = target
        r = [] # result of t - e

        for i, e in enumerate(nums):
            s = t-e # number missing to complement e + s = t
            if s in r:
                return [r.index(s), i ]
            r.append(e)
        return []