class Solution:

    def encode(self, strs: List[str]) -> str:
        k = len(strs)
        l = [0] * k
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        print(s)
        while i < len(s):
            num = ""
            while s[i] != '#':
                num += s[i]
                i += 1
            length = int(num)
            res.append(s[i + 1:i + 1 + length])
            i += length + 1
        return res