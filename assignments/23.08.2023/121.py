class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        max_p = 0
        while r < len(prices):
            currp = prices[r] - prices[l]
            if prices[l] < prices[r]:
                max_p = max(currp,max_p)
            else:
                l = r
            r +=1 
        return max_p
