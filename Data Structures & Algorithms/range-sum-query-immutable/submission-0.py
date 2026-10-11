class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        self.n = len(nums)
        self.prefix = [0] * (self.n + 1)

        for i in range(self.n):
            self.prefix[i+1] = self.prefix[i] + self.nums[i]

        
    def sumRange(self, left: int, right: int) -> int:
        """
        sumRange(left, right) = prefix(right + 1) - prefix(left)
        """
        return self.prefix[right + 1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)