class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        l = []
        r = []
        maxL = 0
        maxR = 0
        res = 0
        # left run

        for i in range(len(h)):
            maxL = max(maxL, h[i])
            l.append(maxL)

        # right run

        for i in range(len(h) - 1 , -1 , -1):
            maxR = max(maxR, h[i])
            r.append(maxR)
        

        r.reverse()
        # compute
        print(f"left:{l},\nright:{r}")

        for i in range(len(h)):
            minC = min(r[i], l[i])
            area = minC - h[i] 
            res += area


        return res

     
            