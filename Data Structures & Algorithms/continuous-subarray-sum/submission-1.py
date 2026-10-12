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


        # setup prefix sum array
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        # {remainder : index}
        remainders = {0 : 0} # edge case, empty prefix sum

        # iterate through prefix sum array
        # add remainders
        for i in range(1, n+1):
            r = prefix[i] % k
            if r not in remainders:
                remainders[r] = i
            else:
                
                # subarray length = current r - already seen r
                if i - remainders[r] >= 2:
                    return True
        return False