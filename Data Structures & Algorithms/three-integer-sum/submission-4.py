class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = sorted(nums)
        res= []
        for i in range(len(a) - 2):
            if i > 0 and a[i] == a[i-1]:
                continue
            l = i+1
            r = len(a) - 1
# [-4,-1,-1,0,1,2]

            while l < r:
                s = a[i] + a[l] + a[r]
                if s == 0:
                    print([i,l,r])
                    res.append([a[i] , a[l] , a[r]])
                    r-=1
                    l+=1
                    while a[l] == a[l-1] and l<r: 
                        l+=1
                    while a[r] == a[r+1] and l<r: 
                        r-=1
                elif s > 0:
                    r-=1
     
                elif s < 0:
                    l +=1
    
        return res
        