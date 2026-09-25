class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        u: 
            return all unique combos that sum == target

            candidates can only be chosen once (NO DUPS)

            return array of all unique combos

        m:
            back tracking dfs problems, but instead of adding duplicates, search a branch once

            when searching a branch, decide to move to next branch or skip/backtrack 

        p:
            since there are duplicates in the list, there is a chance of having duplicate
            combinations. we can continue dfs as usual but when we backtrack, we want to SKIP 
            all duplicates of our current i index. this can be done using a while loop that iterates i index
            forward until no duplicates are found. once we skip all duplicates, we can continue dfs.

        """

        res = []
        candidates.sort()

        def dfs(i, cur, total):

            # base case: target reached
            if total == target:
                res.append(cur.copy())
                return

            # base case: target exceeded or end of list
            if total > target or i >= len(candidates):
                return

            # search new branch
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # backtrack if base case reached
            cur.pop()

            # check if i is in bounds and if there are duplicates, skip before continuing dfs
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # continue dfs 
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
