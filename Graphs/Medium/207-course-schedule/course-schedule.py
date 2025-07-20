from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1) Build adjacency list
        adj = { i: [] for i in range(numCourses) }
        for a, b in prerequisites:
            adj[b].append(a)

        # 2) Prepare visit states
        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = [UNVISITED] * numCourses

        # 3) DFS with cycle detection
        def dfs(u: int) -> bool:
            if state[u] == VISITING:
                # We've circled back onto the recursion stack → cycle!
                return False
            if state[u] == VISITED:
                # Already fully processed; no cycle from here
                return True

            # Mark as exploring
            state[u] = VISITING
            # Explore all “next” courses
            for v in adj[u]:
                if not dfs(v):
                    return False

            # Done exploring this node
            state[u] = VISITED
            return True

        # 4) Run DFS on every course
        for u in range(numCourses):
            if state[u] == UNVISITED:
                if not dfs(u):
                    return False

        return True
