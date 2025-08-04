class Solution:
    def isValid(self, s: str) -> bool:
        # ans = []
        # n = len(s)
        # for i in range(n):
        #     if s[i] == '(' or s[i] == '[' or s[i] == '{':
        #         ans.append(s[i])
        #     elif len(ans)>0:
        #         if s[i] == ')' and ans[-1] == '(':
        #             ans.pop()
        #         elif s[i] == '}' and ans[-1] == '{':
        #             ans.pop()
        #         elif s[i] == ']' and ans[-1] == '[':
        #             ans.pop()
        #         else:
        #             return False
        #     else:
        #         return False
        # return len(ans) == 0

        stack = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif not stack:
                return False
            elif c == ')' or c == ']' or c == '}':
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(c)
        if len(stack) != 0:
            return False
        return True

                