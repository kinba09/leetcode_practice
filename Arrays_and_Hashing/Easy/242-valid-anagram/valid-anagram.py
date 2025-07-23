class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # return False

        s_cont = Counter(s)
        t_cont = Counter(t)

        if len(s_cont) != len(t_cont):
            return False
        for i in s_cont:
            if s_cont[i] != t_cont[i]:
                return False
        return True

            