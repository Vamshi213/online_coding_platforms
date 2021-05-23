class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = ''
        temp1 = ''
        for i in range(len(s)):
            temp += s[i]
            for j in range(len(temp)):
                if temp[j] == s[i] and s[j:i+1] == s[j:i+1][::-1] and len(s[j:i+1]) > len(temp1):
                    temp1 = s[j:i+1]
                    break
        return temp1
