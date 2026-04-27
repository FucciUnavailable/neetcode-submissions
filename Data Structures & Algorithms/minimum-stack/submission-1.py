class MinStack:

    def __init__(self):
        self.stak = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stak.append(val)
        if self.mins and val <= self.mins[-1]:
            self.mins.append(val)
        elif self.mins and val > self.mins[-1]:
            self.mins.append(self.mins[-1])
        elif not self.mins:
            self.mins.append(val)
        print(self.stak)
        print(self.mins)
        
        

    def pop(self) -> None:
        self.stak.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.stak[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
