from heapq import heapify, heappop

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        
        cn = Counter(arr)
        
        
        cn = [-value for value in cn.values()]
        heapify(cn)
        
        
        amount = len(arr)//2 + len(arr) % 2
        counter = 0
        while amount > 0:
            amount += heappop(cn)
            counter += 1
        return counter