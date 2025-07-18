class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #easy and interesting bfs with counting levels
        if not grid:
            return -1
        
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh_count = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count +=1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        #if no fresh then 0
        if fresh_count == 0:
            return 0
        
        while q and fresh_count > 0:

            #layer by layer
            for _ in range(len(q)): 
                r,c = q.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if  (0 <= nr < rows) and (0 <= nc < cols) and (grid[nr][nc] == 1):
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh_count -=1
            minutes+= 1
        
        return minutes if fresh_count == 0 else -1


        
