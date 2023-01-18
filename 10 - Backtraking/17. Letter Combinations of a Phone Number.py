class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        cur = []
        letterMap = {"2":["a", "b", "c"], "3":["d", "e", "f"],
                        "4":["g", "h", "i"], "5":["j", "k", "l"],
                        "6":["m", "n", "o"], "7":["p", "q", "r", "s"],
                        "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}

        def dfs(digitPos):
            if len(cur) == len(digits):
                res.append("".join(cur.copy()))
                return
            
            # for i in range(digitPos, len(digits)): 
            for i in range(len(letterMap[digits[digitPos]])):
                cur.append(letterMap[digits[digitPos]][i])
                dfs(digitPos + 1)
                cur.pop()
        
        dfs(0)
        return res