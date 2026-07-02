class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        #decode the number then add that many elements
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded_strs.append(s[i:j])
            i = j
        return decoded_strs
