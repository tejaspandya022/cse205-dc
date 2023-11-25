class Solution(object):
    def backspaceCompare(self, s, t):
        stack1=[]
        for c in s:
            if c=='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(c)
        stack2=[]
        for a in t:
            if a=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(a)
        if stack1==stack2:
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        