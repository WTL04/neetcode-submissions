class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        # get weaker nodes which have edges pointing to it
        weaker = set()
        for u, v in edges:
            weaker.add(v)

        # champ candidates are nodes not in weaker set
        candidates = [i for i in range(n) if i not in weaker]

        # return -1 if there are more than 1 candidate
        if len(candidates) != 1:
            return -1
        
        return candidates[0]