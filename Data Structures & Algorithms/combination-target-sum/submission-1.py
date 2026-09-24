class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, currentList, total):
            # base case: hit the target
            if total == target:
                res.append(currentList.copy())
                return

            for j in range(i, len(nums)):
                # early stop 
                if total + nums[i] > target:
                    return 

                # add duplicates and search
                currentList.append(nums[j])
                dfs(j, currentList, total + nums[j])

                # backtrack once we exceed target 
                currentList.pop()

        dfs(0, [], 0) 
        return res