class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        t = temperatures
        store = [0] * len(t)
        tmp = []
        for i, e in enumerate(t):
            while tmp and e > t[tmp[-1]]:
                x = tmp.pop()
                store[x] = i -x
            tmp.append(i)
        print(store)
        return store

            
                
