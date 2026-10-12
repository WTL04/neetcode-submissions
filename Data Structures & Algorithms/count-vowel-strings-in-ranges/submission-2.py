class Solution:

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        [ 0, 1, 1, 2, 3, 4]

        m - 
            prefix sum, where the sum is the count of valid vowel strings

        """
        def isValid(c):
            vowels = { 'a', 'e', 'i', 'o', 'u'}
            return c[0] in vowels and c[-1] in vowels

        ans = []
        prefix = [0]

        n = len(words)
        count = 0
        for i in range(n):
            if isValid(words[i]):
                count += 1 
            prefix.append(count)

        for r in queries:
            li = r[0]
            ri = r[1]

            res = prefix[ri + 1] - prefix[li]
            ans.append(res)

        return ans

        # 0, 1, 2, 3, 4, 5

            

            
