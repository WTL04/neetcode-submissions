class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        UMPIRE
        - understand: i have a budget of k, which is the number of 0s i can flip. 

        - match: I know that this is a dynamic sliding window problem because it states 'consecutive', implying it wants a process
        a subarray. Searching for the maximum number of consecutive 1's means that this is NOT a fixed window but a dynamic one, to search for the
        largest subarray of consistent 1's possible

        - plan: 

            have left and right pointer
            maxSize = 0


            for right in range length of nums:

                if right pointer lands on 0:
                    k -= 1

                while k is less than 0:
                    move left pointer
                    
                    if left pointer lands on 0:
                        k += 1

                calculate maxSize

            return maxSize
        """

        l = 0
        maxSize = 0

        for r in range(len(nums)):

            if nums[r] == 0:
                k -= 1

            while k < 0:

                if nums[l] == 0:
                    k += 1

                l += 1

            size = (r - l) + 1
            maxSize = max(size, maxSize)

        return maxSize