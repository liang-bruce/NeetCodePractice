class StockSpanner:

    def __init__(self):
       self.stack = [] 

    def next(self, price: int) -> int:
        # O(1)
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, span])
        return span
        
        # O(n) TLE
        # if len(self.stack) == 0 or self.stack[-1] > price:
        #     self.stack.append(price)
        #     return 1
        # ctr = 1
        # i = len(self.stack) - 1
        # while i >= 0 and self.stack[i] <= price:
        #     ctr += 1
        #     i -= 1
        # self.stack.append(price)
        # return ctr
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)