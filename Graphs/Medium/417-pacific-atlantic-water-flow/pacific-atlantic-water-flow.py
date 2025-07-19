class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m = len(heights)
        n = len(heights[0])
        p_ocean = [[False]*n for _ in range(m)]
        a_ocean = [[False]*n for _ in range(m)]

        def dfs(r: int, c: int, seen: list[list[bool]]):
            seen[r][c] = True
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = dr+r, dc+c
                if (0 <= nr < m and 0 <= nc < n and not seen[nr][nc] and heights[nr][nc] >= heights[r][c]):
                    dfs(nr,nc,seen)

        for i in range(m):
            dfs(i,0,p_ocean)
            dfs(i,n-1,a_ocean)
        for j in range(n):
            dfs(0,j,p_ocean)
            dfs(m-1,j,a_ocean)
        
        result = []
        for i in range(m):
            for j in range(n):
                if p_ocean[i][j] and a_ocean[i][j]:
                    result.append([i,j])
        return result