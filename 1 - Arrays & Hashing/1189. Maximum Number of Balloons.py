class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        validChar = {'b', 'a', 'l', 'o', 'n'}
        count = {c : 0 for c in validChar}

        for s in text:
            if s in validChar:
                count[s] += 1
        
        res = 0
        if count['l'] >= 2 and count['o'] >= 2:
            res = min(count.values())
            res = min(res, count['o'] // 2, count['l'] // 2)
        return res