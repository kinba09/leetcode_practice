class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # num = len(numbers)
        # i=0
        # j = num-1
        # while i < j:
        #     if numbers[i] + numbers[j] == target:
        #         return [i+1,j+1]
        #     elif numbers[i] + numbers[j] > target:
        #         j = j - 1
        #     elif numbers[i] + numbers[j] < target:
        #         i += 1
        
        n = len(numbers)
        left, right = 0 , n-1
        while left < right:
            x = numbers[left] + numbers[right]
            if x == target:
                return [left+1,right+1]
            elif x < target:
                left+=1
            elif x > target:
                right -=1
        