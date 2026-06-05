class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, x in enumerate(nums):
            need = target - x

            if need in d:
                return [d[need], i]

            d[x] = i
