# reader.get(index) is provided by the judge and returns 2147483647 outside the hidden array.
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:

        """
        reader.get(index) reads the current element at given index
        length of secret is unknown
        return index of target
        return -1 if not in secret
        secret is sorted increasing order
        
        search has to be O(logn) - binary search
        """

        low, high = 0, 1

        while True:
            try:
                if reader.get(high) < target:
                    low = high
                    high *= 2
                elif reader.get(high) > target:
                    
                    break
                else:
                    return high

            except IndexError:
                break

        l, r = low, high

        while l <= r:
            mid = (l + r) // 2
            if reader.get(mid) == target:
                return mid

            if reader.get(mid) < target:
                # search right
                l = mid + 1
            
            else:
                # search left
                r = mid - 1


    
        


        return -1
