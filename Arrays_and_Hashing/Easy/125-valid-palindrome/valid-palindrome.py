class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i = 0
        # j = len(s) - 1
        # while i < j:
        #     while i < j and not s[i].isalnum(): i += 1
        #     while i < j and not s[j].isalnum(): j -= 1
        #     if s[i].lower() != s[j].lower(): return False
        #     i += 1
        #     j -= 1
        # return True
        s = ''.join(c.lower() for c in s if c.isalnum())
        left,right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right -=1
        return True