class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        UMPIRE
        understand - smallest possible array that have greater than or equal to sum to the target

        match - sliding window due to finding a subarray, dynamic due to finding minimum size

        plan - 

        left, right = 0, 0
        running_total = 0

        minimum_length = inf

        while l exists:
            expand window when subarray does NOT equal target
            shrink window when subarray is greater than or equal to target
                record current window length 
                compare to minimum_length

        return minimum_length

        review - edge cases:
            1. no such subarray, return 0
        """
        n = len(nums)
        l, r = 0, 0
        total = 0
        min_length = 9999999999

        for r in range(n):
            total += nums[r]
            
            # shrink window
            while total >= target:
                # record min window length
                win_length = (r - l) + 1
                min_length = min(win_length, min_length)

                # shrink window
                total -= nums[l]
                l += 1

        if min_length == 9999999999:
            return 0 

        return min_length


