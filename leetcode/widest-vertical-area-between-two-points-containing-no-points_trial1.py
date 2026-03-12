class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        x = [x for x, y in points]
        x.sort()
        maxWidth  = 0

        for i in range(1,len(x)):
            maxWidth = max(maxWidth, x[i] - x[i-1])
        return maxWidth