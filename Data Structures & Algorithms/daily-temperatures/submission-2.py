class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t= temperatures
        d = []
        res = [0] * len(t)
        for i, e in enumerate(t):
            while d and e > d[-1][1]:
                x = d.pop()
                idx = x[0]
                tm = x[1]
                res[idx] = i - idx
            
            d.append([i,e])
        return res




            
                
