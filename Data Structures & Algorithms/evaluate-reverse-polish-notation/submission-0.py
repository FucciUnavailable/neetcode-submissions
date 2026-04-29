class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        op = {'+','-','*','/'}
        store = []
        for i in tokens:
            if i not in op:
                store.append(i)
            else:
                f = int(store[-1])
                s = int(store[-2])
                if i == '+':
                    store.append(f+s)
                if i =='-':
                    store.append(f-s)
                if i =='/':
                    store.append(f/s)
                if i == '*':
                    store.append(f*s)
        return store[-1]