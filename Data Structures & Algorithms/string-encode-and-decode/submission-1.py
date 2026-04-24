class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f'{len(s)}#{s}' for s in strs)
    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        end = len(s)
        while start < end:
            mover = start
            while mover < end and s[mover] != "#":
                mover +=1
            length = int(s[start:mover])
            mover+=1
            res.append(s[mover:mover+length])
            start = mover + length
        return res