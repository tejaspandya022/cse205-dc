class Solution:
    def maxProduct(self, nums: List[int]) -> int:               
        heap = [-1]
        for num in nums:
            if num > heap[0]:
                if len(heap) == 2:
                    heapq.heappop(heap)
                heapq.heappush(heap, num)
                
        return (heap[0]-1) * (heap[1]-1)