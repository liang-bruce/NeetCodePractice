class Solution:
    def isHappy(self, n: int) -> bool:
        # # mathematical
        # while True:
        #     num = str(n)
        #     n = sum([int(digit) ** 2 for digit in num])
        #     if n < 10:
        #         return True if (n == 1 or n == 7) else False

        # fast-slow pointer - like linked list cycle
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            slow = self.sumSquareDigits(slow)
            fast = self.sumSquareDigits(self.sumSquareDigits(fast))

        return True if fast == 1 else False
        
    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output