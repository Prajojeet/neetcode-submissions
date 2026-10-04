class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adjacency = {i:[] for i in range(n)}
        for s, c, w in edges:
            adjacency[s].append((w, c)) # Store (weight, node connected)

        shortest = {i:float('inf') for i in range(n)}

        q= []
        heapq.heappush(q,(0, src))
        shortest[src] = 0

        while(q):
            dis, node = heapq.heappop(q)
            for w, c in adjacency[node]:
                if dis + w < shortest[c]:
                    shortest[c] = dis + w
                    heapq.heappush(q, (dis + w, c))

        # Edge Case - for non connected nodes, set -1
        for node in shortest:
            if shortest[node] == float('inf'):
                shortest[node] = -1

        return shortest    



    

