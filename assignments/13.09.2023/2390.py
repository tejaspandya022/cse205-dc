class Solution:
    def removeStars(self, s: str) -> str:
        stack1=[]
        for c in s:
            if c=='*':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(c)
        return "".join(stack1)
        