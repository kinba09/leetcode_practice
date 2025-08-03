class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        near = float('inf')
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:

                x = nums[left] + nums[right] + nums[i]
                y = abs(target - x)

                if y < near:
                    near = y
                    ans = x
                    if y == 0:
                        return ans

                if x < target:
                    left +=1
                else:
                    right -=1
        return ans
