class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lp=""
        temp=""
        for i in strs[0]:
            temp+=i
            for j in strs:
                if j.find(temp):
                    temp=""
                    break
            if len(temp)>len(lp):
                lp=temp
        return lp
        
