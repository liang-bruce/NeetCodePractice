# easier to remember - another stack recording each values' corresponding minimum
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# more efficient but harder to remember
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if len(self.minStack) == 0 or val <= self.minStack[-1]:
#             self.minStack.append(val)

#     def pop(self) -> None:
#         if self.stack[-1] == self.minStack[-1]:
#             self.minStack.pop()
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.minStack[-1]
