class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fs = []
        for i,e in zip(position, speed):
            fs.append((i,e))
        cars = sorted(fs, key= lambda x: x[0], reverse=True)
        t = target
        far  = []
        for c in cars:
            ttd = (t - c[0]) / c[1]
            if not far:
                far.append(ttd)
            elif far and far[-1] < ttd:
                far.append(ttd)
           
        print(cars)
        print(far)
        return len(far)

        
            