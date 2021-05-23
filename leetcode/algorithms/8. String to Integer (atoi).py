class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxm = 2**31-1
        minm = -2**31
        count = 0
        sign = 1
        val=0
        digits = '1234567890'
        for i in s:
            if i == " ":
                count+=1
            else:
                break
        if count < len(s):
            if s[count] == '+':
                sign = 1
                count+=1
            elif s[count] == '-':
                sign = -1
                count+=1
        for i in range(count,len(s)):
            if s[i] in digits:
                val=val*10+int(s[i])
            else:
                break
        val=sign*val
        if val>maxm:
            return maxm
        elif val<minm:
            return minm
        else:
            return val
