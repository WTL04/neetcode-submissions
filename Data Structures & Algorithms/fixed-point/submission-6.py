class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        if not arr:
            return -1
        
        if arr[0] == 0:
            return 0

        smallest =  float('inf')
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if mid == arr[mid]:
                # record current smallest
                smallest = min(smallest, arr[mid])
            
            if arr[mid] < mid:
                # search right
                l = mid + 1
            else:
                # search left
                r = mid - 1

        return -1 if smallest == float('inf') else smallest