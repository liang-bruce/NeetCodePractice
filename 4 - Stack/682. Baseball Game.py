class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for oper in operations:
            if oper == "C":
                stack.pop()
            elif oper == "D":
                stack.append(stack[-1] * 2)
            elif oper == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(oper))
        
        return sum(stack)