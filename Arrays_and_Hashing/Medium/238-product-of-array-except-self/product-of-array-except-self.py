class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        surfix = 1
        for i in range(n-1,-1,-1):
            ans[i] = surfix * ans[i]
            surfix *= nums[i]

        return ans