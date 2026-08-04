class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 1
        if len(s) == 0:
            return 0
        z = set()
        l = 0
        r = 0

        while r  < len(s):
            if s[r] not in z:
                z.add(s[r])
                r+=1
                m = max(m, r-l)
            else:
                z.remove(s[l])
                l+=1
        return m

        
