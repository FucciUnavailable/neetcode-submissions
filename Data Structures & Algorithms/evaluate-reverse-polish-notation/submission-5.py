class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        op = {'+','-','*','/'}
        store = []
        for i in tokens:
            if i not in op:
                store.append(int(i))
                
            else:
               
                f = store.pop(-2)
                s = store.pop(-1)
                if i == '+':
                    store.append(f+s)
                if i =='-':
                    store.append(f-s)
                if i =='/':
                    store.append(int(f/s))
                if i == '*':
                    store.append(f*s)
            
     
   
        return store[-1]