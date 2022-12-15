class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encoded = ""
        for element in strs:
            encoded += str(len(element)) + "#" + element
        
        return encoded

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decoded = []
        i = 0
        while i < len(str):
            # find the end of length using another pointer
            j = i
            while str[j] != "#":
                j += 1
            currLength = int(str[i:j])
            decoded.append(str[j + 1: j + 1 + currLength])
            i = j + 1 + currLength
        
        return decoded