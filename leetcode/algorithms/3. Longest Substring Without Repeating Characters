class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=""
        length = 0
        for i in s:
            if i in a:
                if(length < len(a)):
                    length= len(a);
                b=a.find(i)+1
                a=a[b:]
            a+=i
            if(len(a)>length):
                length=len(a)
        return length
