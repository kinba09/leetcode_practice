class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            group[tuple(sorted(word))].append(word)
        return list(group.values())