class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1:
            return s
        pos = 0
        output =[""]*numRows
        plus = True
        
        for letter in s:
            output[pos] = output[pos]+letter
            
            if pos == numRows-1:
                plus=False
            elif pos == 0:
                plus= True
            if plus:
                pos+=1
            else:
                pos-=1
        out="".join(output)
        return out
    
