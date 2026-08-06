class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            x = n
            product = 1

            while x > 0:
                digit = x % 10
                product *= digit
                x //= 10

            if product % t == 0:
                return n

            n += 1