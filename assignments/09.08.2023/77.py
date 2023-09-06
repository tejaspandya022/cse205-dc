
class Solution(object):
   def combine(self, n, k):
        output = []
        def helper(n, k, pos, temp):
            temp = temp or []

            if len(temp) == k:
                output.append(temp[:])
                return

            for i in range(pos, n):
                temp.append(i+1)
                helper(n, k, i+1, temp)
                temp.pop()
        helper(n,k,0,None)
        return output
