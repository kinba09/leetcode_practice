class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        # quick impossibility check (even all substrings is n*(n+1)//2)
        total_substrings = n * (n + 1) // 2
        if k > total_substrings:
            return -1

        def is_active(t: int) -> bool:
            marked = [False] * n
            for idx in order[:t+1]:
                marked[idx] = True

            last_star = -1
            valid = 0
            for i in range(n):
                if marked[i]:
                    last_star = i
                if last_star != -1:
                    valid += (last_star + 1)
                # small early stop
                if valid >= k:
                    return True
            return valid >= k

        lo, hi = -1, n - 1  # first true
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if is_active(mid):
                hi = mid
            else:
                lo = mid

        return hi if is_active(hi) else -1