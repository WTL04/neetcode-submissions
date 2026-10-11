class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = s.count('1')
        result = 0

        # we are computing the number of zeros in 'left score'
        # consequently, we are removing number of ones that show up in 'left score'
        for i in range(len(s) - 1): 
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1

            result = max(result, zeros + ones)

        return result