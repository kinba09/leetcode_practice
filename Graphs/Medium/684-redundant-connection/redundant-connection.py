class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))

        def find(x:int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x]) #find the parent
            return parent[x]
        def union(u:int, v:int) -> bool:
            roota, rootb = find(u), find(v)
            if roota == rootb: # if in loop 
                return False
            parent[rootb] = roota
            return True
        
        ans = []
        for u,v in edges:
            if not union(u,v):
                ans = [u,v]
        return ans
            