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
                e = st.pop()
                if pas[e] != i:
                    return False
        return st == []