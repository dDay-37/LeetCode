class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        before = [float('inf') for _ in range(n)]
        before[src]=0
        after = before[:]
        for i in range(k+1):
            after = before.copy()
            for fr,to,cs in flights:
                if before[fr]==float('inf'):
                    continue
                if before[fr] + cs < after[to]:
                    after[to] = before[fr] + cs
            before = after
        return after[dst] if after[dst] != float('inf') else -1