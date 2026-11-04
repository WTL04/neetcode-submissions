class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        naive recursiv solution
        - time: O(2^n)
        - space: O(n)
        """

        # key: i, value, total
        memo = {}

        def dfs(i, total):

            # reached the end of the list
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            if (i, total) in memo:
                return memo[(i, total)]

            # search add and subtracking sub trees 
            memo[(i, total)] = dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i])

            return memo[(i, total)]
            

        return dfs(0, 0)
