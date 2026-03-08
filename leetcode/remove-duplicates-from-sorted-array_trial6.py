class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        0 == 1 true remove 1

        """
        left = 0
        n = len(nums)
        for right in range(1,n):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]       
        return left + 1
        