class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=str(x)
        if(a[0] == '-' or a[0] == '+'):
            b=a[0]+a[1:][::-1]
        else:
            b=a[::-1]
        k=int(b)
        if(-(2**31) <= k <= (2**31)-1):
            return k
        else:
            return 0
            
