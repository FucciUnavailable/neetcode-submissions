class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l = 0
        ls = 0

        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            
            mC = max(charMap.values())
            limit = r - l - mC + 1
            if limit > k:
                charMap[s[l]] -= 1
                l += 1         
            else:
                ls = max(ls, r-l+1)
                
        return ls