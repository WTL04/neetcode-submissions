class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        u:
            all possible subsets means all possible combinations within nums

            empty array also counts as a subset

            no duplicate subsets

            return an array of subsets, order does not matter

        m: 
            this can be a 'tree' problem where we create a decision tree that checks
            if we should 'add' or 'not add' a number to a subset. This lets us
            check all possible subsets

        """

        res = []
        subset = []

        def dfs(i):
            # base case: index out of bounds
            if i >= len(nums):
                res.append(subset.copy())
                return 

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res