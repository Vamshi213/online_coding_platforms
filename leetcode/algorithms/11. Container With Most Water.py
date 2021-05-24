class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        out = 0
        for i in range(len(height)-1,0,-1):
            out = max(out, i*min(height[0],height[-1]))
            if height[0]<height[-1]: height.pop(0)
            else: height.pop()
        return out
