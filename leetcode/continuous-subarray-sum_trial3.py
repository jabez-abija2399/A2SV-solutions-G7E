class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainderMap = {0:-1}
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            remainder = prefixSum % k
            if remainder in remainderMap:
                if i - remainderMap[remainder] >= 2:
                    return True
            else:
                remainderMap[remainder] = i
        return False
