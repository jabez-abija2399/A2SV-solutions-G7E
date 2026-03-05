class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        targets = []
        for i in range(len(nums)):
            if nums[i] == target:
                targets.append(i)
        return targets