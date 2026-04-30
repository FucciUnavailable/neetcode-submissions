class Solution:
    def isValid(self, s: str) -> bool:
        pas = {
        '[':']', 
        '(':')', 
        '{':'}'
        }
        st = []
        for i in s:
            if i in pas:
                st.append(i)
            else:
                if not st:
                    return False
                d= st.pop()
                if pas[d] != i:
                    return False
        return not st
            