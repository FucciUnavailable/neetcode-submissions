class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tree = {}

        for n in nums:
            tree[n] = tree.get(n, 0) + 1
        
        sortedt = sorted(tree.keys(), key=lambda x:tree[x], reverse=True)
        return sortedt[:k]