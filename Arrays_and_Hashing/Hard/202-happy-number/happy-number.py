class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        def nxt_number(x:int) -> int:
            summ = 0
            while x:
                temp = x%10
                temp2 = temp*temp
                x = x//10
                summ += temp2

            return summ
        while n != 1:
            if n in check: return False
            check.add(n)
            n = nxt_number(n)
        return True
        

            
