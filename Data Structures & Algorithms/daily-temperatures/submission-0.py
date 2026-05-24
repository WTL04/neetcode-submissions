class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        monotonic decreasing stack
        - only push values that are decreasing
        - if not decreasing, pop until monotonic order is valid, then push

        when increasing value is found
        - compute index distance with bottom of stack and top of stack

        """

        n = len(temperatures)
        stack = [] # monotonic decreasing
        results = [0] * n # stores index distances

        # no elements
        if not temperatures:
            return results

        for i in range(n):
            temp = temperatures[i]

            # remove values less than temp
            while stack and temp > temperatures[stack[-1]]:
                removed = stack.pop()

                distance = i - removed

                results[removed] = distance

            # append once all less values are removed
            stack.append(i)

        return results