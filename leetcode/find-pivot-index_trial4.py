class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        totalSum = sum(nums)
        for i in range(len(nums)):
           if leftSum == totalSum - leftSum - nums[i]:
              return i
           leftSum += nums[i]
        return -1
        