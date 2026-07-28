class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l+=1
            while not s[r].isalnum() and l < r:
                r-=1
            sr = s[r].lower()  
            sl = s[l].lower()

            if sl != sr:
                return False
            l+=1
            r-=1
        return True