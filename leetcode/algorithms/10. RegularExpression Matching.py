class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        x= re.findall(p,s)
        if s in x:
            return True
        else:
            return False
