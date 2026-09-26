class Solution:
    def __init__(self):
        self.separator = "#"

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = str(len(string))
            encoded = encoded + length + self.separator + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i<len(s):
            next_separator = s.find(self.separator, i)
            word_length = int(s[i:next_separator])
            word = s[next_separator+1 : next_separator+1+word_length]
            decoded.append(word)
            i = next_separator + 1 + word_length
        return decoded