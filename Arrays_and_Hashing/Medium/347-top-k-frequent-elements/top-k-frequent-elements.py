class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  count = Counter(nums)
        #  return [items for items,freq in count.most_common(k)]
       
        # arr = Counter(nums)
        # sorted_items = sorted(arr.items(), key=lambda kv: kv[1], reverse=True)
        # ans = []
        # for i in range(k):
        #      # sorted_items[i] is (num, freq), so take [0] for the num
        #     ans.append(sorted_items[i][0])
        # return ans


        #bucket_sort
        freq = Counter(nums)
        n = len(nums)
        arr: list[list[int]] = [[] for _ in range(n+1)]
        for val,num in freq.items():
            arr[num].append(val)
        ans = []
        for i in range(n,0,-1):
            for val in arr[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans
        return ans
        



