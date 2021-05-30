class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        out=""
        for i in range(0,len(s)):
            k=indices.index(i)
            out+=s[k]
        return out
