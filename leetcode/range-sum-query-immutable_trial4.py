class NumArray:

    def __init__(self, nums: List[int]):
        self.prifix = [0] * (len(nums) + 1)
        for i in  range(len(nums)):
            self.prifix[i+1] = self.prifix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prifix[right + 1] - self.prifix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)