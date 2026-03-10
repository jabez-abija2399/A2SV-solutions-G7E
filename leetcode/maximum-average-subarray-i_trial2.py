class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        1, 12, -5 -6, 50 , 3
        4
        5
        1, 12, -5 -6 = 2
        12, -5, -6 , 50 = 49 + 2 = 51
        -5. -6, 50, 3 = 3 - 12 = -9 + 51 = 42

         1, 12, -5 -6, 50 , 3, 4, 4
         
         6 = 3
         7 = 4
         8 = 5
         9 = 6
        """
        curSum = sum(nums[:k])
        maxSum = curSum
        for i in range(k, len(nums)):
            curSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, curSum)
        return maxSum / float(k)