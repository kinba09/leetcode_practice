class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  count = Counter(nums)
        #  return [items for items,freq in count.most_common(k)]
        arr = Counter(nums)
        sorted_items = sorted(arr.items(), key=lambda kv: kv[1], reverse=True)
        ans = []
        for i in range(k):
             # sorted_items[i] is (num, freq), so take [0] for the num
            ans.append(sorted_items[i][0])
        return ans




