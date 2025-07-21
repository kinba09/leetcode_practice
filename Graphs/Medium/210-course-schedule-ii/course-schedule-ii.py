class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            in_degree[a] +=1

        q = deque(i for i in range(numCourses) if in_degree[i] == 0)
        order = []

        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                in_degree[v] -=1
                if in_degree[v] == 0:
                    q.append(v)
        
        #to check if its a cycle
        return order if len(order) == numCourses else []