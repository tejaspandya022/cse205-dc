class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for a in operations:
            if a=='D':
                stack.append(int(stack[-1])*2)
            elif a=='C':
                stack.pop()
            elif a=='+':
                stack.append(int(stack[-1]+stack[-2]))
            else:
                stack.append(int(a))
        return sum(stack)

        """
        :type operations: List[str]
        :rtype: int
        """
        