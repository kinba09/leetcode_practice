class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        best_area = 0
        current_area = 0

        def dfs(r: int, c: int) -> None:
            nonlocal current_area, best_area
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 
            
            grid[r][c] = 0
            current_area += 1
            best_area = max(best_area,current_area)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = 0
                    dfs(r,c)
        return best_area
