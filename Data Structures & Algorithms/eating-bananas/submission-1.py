class Solution:

    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            The idea: The answer k lies between 1 and max(piles),
            so we binary search over possible speeds: pick a middle k,
            check if it finishes all piles within h hours — if too slow, search faster;
            if it fits, remember it and try slower. 
            The smallest speed that still finishes in time is the answer.
        
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
