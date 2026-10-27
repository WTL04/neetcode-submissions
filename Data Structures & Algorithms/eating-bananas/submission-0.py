class Solution:

    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        u - 
            eating per hour for one pile = k
            limit amount of hours = h

            find min value k
        """
        import math

        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            total_time = 0

            for pile in piles:
                # calculate total time to eat with k rate 
                time_per_pile = math.ceil(pile / k)
                total_time += time_per_pile

            # rate is too slow, look for fast rate
            if total_time > h:
                l = k + 1
            else:
            # rate is good, look for smaller
                r = k

        return r
