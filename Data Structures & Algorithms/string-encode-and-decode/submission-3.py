class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += s
            encoded += "þ" # delimiter

        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        substring = ""

        for char in s:
            if char == "þ":
                res.append(substring)
                substring = ""
            else:
                substring += char

        return res
