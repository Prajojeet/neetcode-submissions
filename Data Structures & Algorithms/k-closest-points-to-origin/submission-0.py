class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate the distance and heapify at the same time!
        
        heap=[]

        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(heap, (-distance,[x,y]))
            if len(heap)>k:
                heapq.heappop(heap)

        return [point for _, point in heap]