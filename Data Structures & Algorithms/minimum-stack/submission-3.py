class MinStack:

    def __init__(self):
        self.stak = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stak.append(val)
        if self.mins:
            cur = self.mins[-1]
            self.mins.append(min(val,cur))
        else:
            self.mins.append(val)

        
        

    def pop(self) -> None:
        self.stak.pop()
        self.mins.pop()
        

    def top(self) -> int:
        if self.stak:
            return self.stak[-1]
        else:
            return null
        

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]
        else:
            return null
        
