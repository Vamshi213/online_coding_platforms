class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1:
            return False
        bo = True
        a=['(','[','{']
        b=[')',']','}']
        par=""
        for i in range(0,len(s)):
            if s[i] in a:
                par+=s[i]
            else:
                if par=="":
                    bo= False
                    break
                k=a.index(par[-1])
                p=b.index(s[i])
                if k!=p:
                    bo= False
                    break
                else:
                    par=par[0:len(par)-1]
        if par=="" and bo:
            return True
        else:
            return False
