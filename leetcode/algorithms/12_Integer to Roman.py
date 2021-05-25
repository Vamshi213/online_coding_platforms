class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        rv = { 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM' }
        result=""
        unit=1
        while num>0:
            rem=num%10
            if rem in (1,2,3):
                result=rv[unit]*rem+result
            elif rem in (6,7,8):
                result=rv[5*unit]+rv[unit]*(rem-5)+result
            elif rem in (4,5,9):
                result=rv[rem*unit]+result
            num=num//10
            unit*=10
        return result
