class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        n = len(nums)

        maxWind = 0
        left = 0
        for right in range(n):
            while nums[right] - nums[left] > n - 1:
                left += 1
            maxWind = max(maxWind, right - left + 1)

        return n - maxWind