class Solution:
    def isValid(self, s: str) -> bool:
        co = {
        ")":"(", 
        "}":"{",
        "]":"["
        }
        t = []

        for i in s:
            
            if i in co:
                
                if not t:
                    return False
                z = t.pop()
                
                if  z != co[i]:
                    return False
            else:
                t.append(i)
        return not t 