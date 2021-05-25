class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rv={'I':1, 'V': 5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for i in range(0,len(s)):
            if i+1 < len(s) and rv[s[i]]<rv[s[i+1]]:
                num=num-rv[s[i]]
            else:
                num+=rv[s[i]]
        return num
