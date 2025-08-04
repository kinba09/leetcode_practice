class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # left_max = [0] * n
        # mx =0
        # for i in range(n):
        #     mx = max(mx,height[i])
        #     left_max[i] = mx
        
        # right_max = [0] * n
        # mx = 0
        # for i in range(n-1,-1,-1):
        #     mx = max(mx,height[i])
        #     right_max[i] = mx
        
        # water = 0
        # for i in range(n):
        #     water += min(right_max[i],left_max[i]) - height[i]
        # return water

        n = len(height)
        left, right = 0, n-1
        ans = 0
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                ans += left_max - height[left]
                left +=1
                left_max = max(left_max,height[left])
            else:
                ans += right_max - height[right]
                right -=1
                right_max = max(right_max,height[right])
        return ans