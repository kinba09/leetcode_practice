class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #o(n)
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False

        #o(nk) where k is the slicing worstcase o(n2) doesnt work
        # n = len(nums)
        # if k >= n:
        #     return len(nums) != len(set(nums))
        # start = 0
        # for i in range(k,n):
        #     if len(nums[start:i+1]) != len(set(nums[start:i+1])):
        #         return True
        #     start +=1
        # return False

        
