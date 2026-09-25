class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        u: 
            we are appending a subtring of t to s, so that s has the same characters as t

            the minimum number of characters in t's substring has to be appened,
            so t could be appened entirely to s, only if any other minimum possibilities
            do not exist.

        m: 

        p:

            s pointer
            t pointer
            
            result = []
            while s pointer or t pointer

                if s and t chars are not the same
                    append to result to record substring
                    iterate t forwards 


                if they are the same
                    iterate s forward
                    iterate t forward
        
            return result             

        """

        # edge case, t is already a substring in s
        if t in s:
            return 0

        s_p, t_p = 0, 0
        res = 0

        while s_p < len(s) and t_p < len(t):
            s_char = s[s_p]
            t_char = t[t_p]

            if s_char == t_char:
                s_p += 1
                t_p += 1
            
            else:
                s_p += 1

        # record leftover substring length
        while t_p < len(t):
            t_p += 1
            res += 1

        return res
            


