from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj=[]
        for i in range(n):
            adj.append([])
        for edge in edges:
            x=edge[0]
            y=edge[1]
            adj[x].append(y)
            adj[y].append(x)

        visited=[False]*n
        q=deque()

        # base case
        if source==destination:
            return True
        q.append(source)
        visited[source]=True
        while q:
            front=q.popleft()
            for x in adj[front]:
                if not visited[x]:
                    q.append(x)
                    visited[x]=True
            if front==destination:
                return True
        else:
            return False