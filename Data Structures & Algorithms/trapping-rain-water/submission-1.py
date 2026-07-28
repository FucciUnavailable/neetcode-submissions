class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        bestL = []
        bestR = []
        maxL = 0
        maxR = 0
        t = 0
        # left pass
        for l in range(len(h)):
            maxL = max(maxL,h[l])
            bestL.append(maxL)
        
        # right pass
        for r in range(len(h) - 1, -1, -1):
            maxR = max(maxR, h[r])
            bestR.append(maxR)
        bestR.reverse()    
        #compute
        for i in range(len(h)):
            bestC = min(bestR[i], bestL[i])
            t+= bestC - h[i]

        return t

     
        print(bestL, bestR)
            