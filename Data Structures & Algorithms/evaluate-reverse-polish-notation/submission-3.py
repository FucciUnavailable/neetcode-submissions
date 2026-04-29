class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        op = {'+','-','*','/'}
        store = []
        for i in tokens:
            if i not in op:
                store.append(int(i))
            else:
                f = store[-2]
                s = store[-1]
                if i == '+':
                    store.append(f+s)
                if i =='-':
                    store.append(f-s)
                if i =='/':
                    store.append(f//s)
                if i == '*':
                    store.append(f*s)
                store.remove(f)
                store.remove(s)
        print(store)
        return store[-1]