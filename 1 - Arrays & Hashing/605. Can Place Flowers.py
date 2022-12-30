class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
       
        for i in range(1, len(f) - 1):  # skip first & last
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0

        # temp = [0] + flowerbed + [0]
        # i = 0
        # while i < len(temp) - 2:
        #     if temp[i] == 0:
        #         if temp[i + 1] == 0:
        #             if temp[i + 2] == 0:
        #                 n -= 1
        #                 temp[i + 1] = 1
        #                 i += 1
        #     i += 1
        # return False if n > 0 else True