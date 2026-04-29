class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        op = {'+','-','*','/'}
        store = []
        for i in tokens:
            if i not in op:
                store.append(i)
            else:
                f = int(store[-2])
                s = int(store[-1])
                if i == '+':
                    store.append(f+s)
                if i =='-':
                    store.append(f-s)
                if i =='/':
                    store.append(f/s)
                if i == '*':
                    store.append(f*s)
        print(store)
        return store[-1]