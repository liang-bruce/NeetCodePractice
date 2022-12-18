class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheseMap = {")": "(", "]": "[", "}": "{"}
        openningP = parentheseMap.values()
        # stack using list
        stack = []
        for i, c in enumerate(s):
            if len(stack) == 0 or c in openningP:
                stack.append(c)
            if c in parentheseMap:
                if stack[-1] == parentheseMap[c]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        return False