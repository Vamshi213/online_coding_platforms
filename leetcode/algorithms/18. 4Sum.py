class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l=len(nums)
        nums.sort()
        result=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                start=j+1
                end=l-1
                while start < end:
                    if nums[i]+nums[j]+nums[start]+nums[end]==target:
                        k=[nums[i],nums[j],nums[start],nums[end]]
                        if k not in result:
                            result.append(k)
                        start+=1
                        end-=1
                    elif nums[start]+nums[end]>target-nums[i]-nums[j]:
                        end-=1
                    else:
                        start+=1
        return result
