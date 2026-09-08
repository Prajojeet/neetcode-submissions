class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # The nlogn heap solution
        result=[]
        for x in nums:
            heapq.heappush(result,x)
            # I want atleast k elements in the heap
            if len(result)>k:
                heapq.heappop(result)
            
        return heapq.heappop(result)