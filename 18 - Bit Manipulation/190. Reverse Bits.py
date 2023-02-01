class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            curBit = (n >> i) & 1
            res = res | (curBit << 31 - i)
        
        return res