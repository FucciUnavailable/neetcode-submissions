class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate pivots
                continue

            L, R = i + 1, len(nums) - 1

            while L < R:
                total = nums[i] + nums[L] + nums[R]

                if total == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]: L += 1  # skip dup L
                    while L < R and nums[R] == nums[R - 1]: R -= 1  # skip dup R
                    L += 1
                    R -= 1
                elif total > 0:
                    R -= 1
                else:
                    L += 1

        return res