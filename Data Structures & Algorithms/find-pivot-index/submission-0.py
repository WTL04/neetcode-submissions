class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        u - 
            [1,7,3,6,5,6]

            output 6 because leftsum = 1+7+3 = 11, rightsum = 5+6 = 11

            find the index where left sum == right sum

        m -
            computing a lot of sums, can use prefix sum 

        p - 

            compute a prefix sum array

            [1,7,3,6,5,6]

            [0, 1, 8, 11, 17, 22, 28]

            leftsum = prefix[i]
            rightsum = prefix[n] - prefix[i+1]

            we do prefix[i+1] in rightsum to not add the pivot 

        """
        n = len(nums)
        prefix = [0] * (n+1) # prefix is always 1 length longer than nums since prefix[0] = 0

        # add prefix sums to prefix
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(n):
            leftSum = prefix[i]
            rightSum = prefix[n] - prefix[i+1]
            if leftSum == rightSum:
                return i

        return -1