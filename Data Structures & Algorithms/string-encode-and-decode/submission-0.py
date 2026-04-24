class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)
    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        total = len(s)
        while start < total:
            end = start
            while end < total and s[end]!= "#":
                end +=1
            length = int(s[start:end])
            end +=1
            res.append(s[end:end+length])

            start = end + length

        return res