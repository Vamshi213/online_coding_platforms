class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        med=nums1+nums2
        med.sort()
        length=len(med)
        if(length%2==0):
            return float((med[length/2]+med[(length/2)-1]))/2
            
        else:
            return float(med[length/2])
