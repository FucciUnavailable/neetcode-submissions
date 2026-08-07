class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        limit = len(s1)
        l = 0
        base = sorted(s1)
        r = len(s1)

        for l in range(len(s2)):
            if s2[l] in base:
                c = s2[l: l+r]
                sC = sorted(c)
                if sC == base:
                    return True

        return False