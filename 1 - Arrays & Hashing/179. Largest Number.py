class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        numStr = [str(n) for n in nums]
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        
        numStr = sorted(numStr, key=cmp_to_key(compare))
        res = "".join(numStr)

        return "0" if res[0] == "0" else res