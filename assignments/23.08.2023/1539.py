class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        i=0 
        j=0
        skip=[]

        while i<n:
            if arr[i]!=j:
                skip.append(j)
                j=j+1
            else:
                i=i+1
                j=j+1
        return skip