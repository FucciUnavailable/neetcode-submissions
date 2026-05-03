class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        tmp = [] # tmp:i
        store = [0] * len(t)

        for i,e in enumerate(t):
            while tmp and e > tmp[-1][0]:
                d = tmp.pop()
                store[d[1]] = i - d[1]
            tmp.append([e,i])
        print(tmp)
        return store
