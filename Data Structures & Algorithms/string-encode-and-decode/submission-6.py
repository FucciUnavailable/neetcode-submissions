class Solution:

    def encode(self, strs: List[str]) -> str:
        t = ""
        for s in strs:
            t += str(len(s))+"#"+s
        return t
    def decode(self, s: str) -> List[str]:
        res = []
        deli = []
        p = 0
        while p < len(s):
            while s[p] != '#':
                deli.append(s[p])
                print(deli)
                p+=1
            word_l = int("".join(deli))
            res.append(s[p+1:word_l+p+1])
            p+= word_l + 1
            deli = []
        return res