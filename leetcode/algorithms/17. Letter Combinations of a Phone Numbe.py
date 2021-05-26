class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digi={'2' : ['a','b','c'],
        '3' : ['d','e','f'],
        '4': ['g','h','i'],
        '5' : ['j','k','l'],
        '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9' : ['w','x','y','z']}
        
        val=[]
        if len(digits) == 1:
            return digi[digits]
        elif len(digits)==0:
            return []
        else:
            res=digi[digits[0]]
            for i in range(1,len(digits)):
                p=digi[digits[i]]
                temp=[]
                for j in range(0,len(res)):
                    for k in range(0,len(p)):
                        str1=res[j]+p[k]
                        temp.append(str1)
                res=temp   
            return res
                
            
