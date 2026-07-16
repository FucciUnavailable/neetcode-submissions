class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = sorted(nums)
        res = []

        for i in range(len(a) -2):
            if i > 0 and a[i] == a[i-1]:
                continue
            l = i +1
            r = len(a) - 1
            while l < r:
                s = a[l] + a[r] + a[i]
                if s == 0:
                    res.append([a[i], a[l], a[r]])
                    l+=1
                    r-=1
                    while l < r and a[l] == a[l-1]:
                        l+=1
                    while l < r and a[r] == a[r+1]:
                        r-=1
                elif s > 0:
                    r-=1
                else:
                    l+=1
        return res