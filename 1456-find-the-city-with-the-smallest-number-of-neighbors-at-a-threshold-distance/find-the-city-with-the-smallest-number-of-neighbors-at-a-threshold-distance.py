class Solution(object):
    def findTheCity(self, n, edges, d):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        def dijk(src):
            dist=[float('inf')]*n
            dist[src]=0
            heap=[(0,src)]
            while heap:
                d,u=heapq.heappop(heap)
                if d>dist[u]:
                    continue
                for v,w in adj[u]:
                    if dist[u]+w<dist[v]:
                        dist[v]=dist[u]+w
                        heapq.heappush(heap,(dist[v],v))
            return dist

        mn=n
        ans=-1
        for i in range(n):
            c=sum(1 for h in dijk(i) if h<=d)
            if c<=mn:
                mn=c
                ans=i
        return ans
        