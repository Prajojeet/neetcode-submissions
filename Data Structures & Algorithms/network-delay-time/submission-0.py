class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = {i:[] for i in range(1, n + 1)}
        for src, conn, ti in times:
            adjacency[src].append((ti, conn))
        
        shortest = {i:float('inf') for i in range(1, n + 1)}
        shortest[k] = 0

        q = []
        heapq.heappush(q, (0, k))

        while(q):
            iti, src = heapq.heappop(q)
            for ti, conn in adjacency[src]:
                if iti + ti < shortest[conn]:
                    shortest[conn] = ti + iti
                    heapq.heappush(q, (ti + iti, conn))

        maximum = max(item for item in shortest.values())

        if maximum == float('inf'):
            return -1 
        return maximum
        
