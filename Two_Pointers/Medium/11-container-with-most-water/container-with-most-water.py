class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height) - 1 
        current = 0
        ans = 0
        while i < j:
            current = min(height[i],height[j]) * (j-i)
            ans = max(ans,current)
            if height[i] < height[j]:
                i += 1
            else: j -= 1
        return ans
