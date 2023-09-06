class Solution(object):
    def smallestEvenMultiple(self, n):
        num3 = n/2
        num4 = n*2
        if n%2!=0:
            return(num4)
        else:
            return(n)