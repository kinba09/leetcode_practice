class Solution:
    def validPalindrome(self, s: str) -> bool:
        #didnt work for this case "eceec" must use recursion
        # n = len(s)
        # left, right = 0,n-1
        # count = 1
        # while left < right:
        #     if s[left] != s[right] and count == 1:
        #         if s[left] == s[right-1]:
        #             count -=1
        #             right -=1
        #         elif s[left+1] == s[right]:
        #             count -=1
        #             left +=1
        #         else:
        #             return False
        #     elif s[left] != s[right] and count == 0:
        #         return False
        #     left += 1
        #     right -=1
        # return True

        #but i am using iterative 
        n = len(s)
        left,right = 0,n-1
        while left < right and s[left] == s[right]:
            left +=1
            right -=1

        if left >= right:
            return True
        
        i,j= left +1, right
        while i<j and s[i] == s[j]:
            i+=1
            j -=1
        if i >= j:
            return True

        i,j= left, right-1
        while i<j and s[i] == s[j]:
            i+=1
            j -=1
        if i >= j:
            return True
        return False