class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        
        m = len(board)
        n = len(board[0])

        def dfs(r:int, c:int):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = '#'

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc)
        
        for r in range(m):
            dfs(r,0)
            dfs(r,n-1)
        for c in range(n):
            dfs(0,c)
            dfs(m-1,c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O' 

