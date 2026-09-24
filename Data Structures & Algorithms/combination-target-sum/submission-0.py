class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currentList, total):
            # base case: hit the target
            if total == target:
                res.append(currentList.copy())
                return

            # base case: miss the target or reached end of list
            if total > target or i >= len(nums):
                return

            # add duplicates
            currentList.append(nums[i])
            dfs(i, currentList, total + nums[i])

            # backtrack once one of the two base cases reached
            # search new 'branch'
            currentList.pop()
            dfs(i + 1, currentList, total)

        dfs(0, [], 0) 
        return res