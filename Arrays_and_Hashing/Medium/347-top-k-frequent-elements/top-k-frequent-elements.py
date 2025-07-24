class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         count = Counter(nums)
         return [items for items,freq in count.most_common(k)]


