class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1
        nums.sort()
        numPairs = 0
        while left < right:
            if nums[left] + nums[right] < target:
                numPairs += (right - left)
                left += 1
            else:
                right -= 1
        return numPairs
