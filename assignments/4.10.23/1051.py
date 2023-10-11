class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        l = len(expected)
        lst = [i for i in range(l) if heights[i]!=expected[i]]
        return (len(lst))