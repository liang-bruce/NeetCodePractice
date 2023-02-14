class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())

        top = self.q1.popleft()

        for i in range(len(self.q2)):
            self.q1.append(self.q2.popleft())

        return top

    def top(self) -> int:
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        
        top = self.q1[0]

        self.q2.append(self.q1.popleft())
        for i in range(len(self.q2)):
            self.q1.append(self.q2.popleft())
        
        return top


    def empty(self) -> bool:
        return True if len(self.q1) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()