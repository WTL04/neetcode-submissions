class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        nums needs to be in range 0 to n
        edge: if first number is greater than 0, return 0
        
        '''
        n = len(nums)

        num_sum = sum(nums)
        total = n * (1 + n) // 2

        return total - num_sum