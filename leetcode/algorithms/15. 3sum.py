class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tri=[]
        if len(nums)<3:
            return tri
        else:
            nums.sort()
            l=len(nums)
            res=[]
            for i in range(0,l):
                j=i+1
                k=l-1
                temp=0-nums[i]
                while j < k:
                    if nums[i]+nums[j]+nums[k]==0 and [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                        j+=1
                        k-=1
                    elif nums[j]+nums[k]>temp:
                        k-=1
                    else:
                        j+=1
            return res
