class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[0,1]
        for i in range(2,n+1):
            a.append(a[i-2]+a[i-1])
        return a[n]
