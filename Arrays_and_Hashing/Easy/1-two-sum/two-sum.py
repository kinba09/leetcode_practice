class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i,num in enumerate(nums):
            to_find = target - num
            if to_find in x:
                return [i,x[to_find]]
            x[num] = i