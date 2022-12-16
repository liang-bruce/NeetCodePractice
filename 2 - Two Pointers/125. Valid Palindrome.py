class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        i = 0
        j = len(s) - 1
        while i < j :
            if s[i].isalnum() & s[j].isalnum():
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            elif not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
        
        return True