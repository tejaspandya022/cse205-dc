class Solution(object):
    def isValid(self, s):
        while '()' in s or '{}' in s or '[]' in s:
            s=s.replace('()','').replace('[]','').replace('[]','')
        return True if len(s)==0 else False
        """
        :type s: str
        :rtype: bool
        """
        