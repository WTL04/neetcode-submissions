class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)

        if n <= 1:
            return True

        for i in range(n-1):
            if nums[i] + 1 != nums[i + 1]:
                return False

        return True
        