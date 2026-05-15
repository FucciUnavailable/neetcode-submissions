class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {} # ab: [ab,ba]
        res = []
        for i in strs:
            nw = "".join(sorted(i))
            
            if nw in s:
                s[nw].append(i)
            else:
                s[nw] = [i]
        for e in s:
            res.append(s[e])
        return res
        