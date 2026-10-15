class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        0 jump means im stuck
        a 'jump' is a jump in indices

        """
        n = len(nums)

        # goal is last index
        goal = n - 1

        # start i at second to last index
        for i in range(n - 2, -1, -1):

            # if current position + jump power is greater than goal index
            # that means the jump is possible to reach goal
            if i + nums[i] >= goal:

                # move goal to next index
                goal = i

        # did we reach the 'end'?
        return goal == 0
            

        

          