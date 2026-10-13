class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image) # rows
        m = len(image[0]) # cols
        orig_color = image[sr][sc]

        # edge case: image already filled
        if orig_color == color:
            return image

        def isValid(r, c):
            return r >= 0 and r < n and c >= 0 and c < m and image[r][c] == orig_color

        def dfs(r, c):
            if not isValid(r, c):
                return

            image[r][c] = color

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)
        return image