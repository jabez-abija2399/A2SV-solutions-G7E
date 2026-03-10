class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        -4, -1,  1, 2

        """
        nums.sort()

        closest = sum(nums[0:3])
        n = len(nums)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if abs(currentSum - target) < abs(closest - target):
                    closest = currentSum
                if currentSum > target:   
                    right -= 1
                elif currentSum < target:
                    left += 1
                else:
                    return target
        return closest

