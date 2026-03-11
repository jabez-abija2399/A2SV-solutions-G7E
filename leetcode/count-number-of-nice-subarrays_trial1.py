class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        odd = 0
        left = 0
        nice = 0
        result = 0
        for right in range(len(nums)):
            
            if nums[right] % 2 == 1:
                odd += 1
                nice = 0
            
            while odd == k:
                nice += 1
                if nums[left] % 2 == 1:
                    odd -= 1
                left += 1
            result += nice
        
        return result