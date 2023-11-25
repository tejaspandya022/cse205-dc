class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:]=list(zip(*matrix[::-1]))        
        """
        Do not return anything, modify matrix in-place instead.
        """
        