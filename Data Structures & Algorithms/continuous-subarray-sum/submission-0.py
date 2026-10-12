class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """

        u - ONLY returning bool
        m - 
            prefix sum and hash map

        p - 

            the trick is:

            A = prefix[i]
            B = prefix[j] 

            if A % k == B % k, 
                that means they share the same multiple 

            if they share the same multiple, there exists a subarray
            with a sum that is a multiple of k

            a hash map is used to store the {remaider : index}, mainly to 
            see if the subarray length >= 2 by checking if index > 2
        """

        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        remainders = {0 : 0} # edge case, empty prefix sum

        # iterate through prefix sum array
        for i in range(1, n+1):
            remainder = prefix[i] % k
            if remainder not in remainders:
                # {remainder : index}
                remainders[remainder] = i

            else:
                # subarray length >= 2
                if i - remainders[remainder] >= 2:
                    return True
        return False