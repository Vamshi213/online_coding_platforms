class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l=len(nums)
        tar=[]
        for i in range(0,l):
            j=i+1
            k=l-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==target:
                    return target
                else:
                    if nums[i]+nums[j]+nums[k] not in tar:
                        tar.append(nums[i]+nums[j]+nums[k])
                if nums[j]+nums[k]>target-nums[i]:
                    k-=1
                else:
                    j+=1
        return tar[min(range(len(tar)), key = lambda i:abs(tar[i]-target))]
        
