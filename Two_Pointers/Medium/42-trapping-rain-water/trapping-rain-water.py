class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        mx =0
        for i in range(n):
            mx = max(mx,height[i])
            left_max[i] = mx
        
        right_max = [0] * n
        mx = 0
        for i in range(n-1,-1,-1):
            mx = max(mx,height[i])
            right_max[i] = mx
        
        water = 0
        for i in range(n):
            water += min(right_max[i],left_max[i]) - height[i]
        return water