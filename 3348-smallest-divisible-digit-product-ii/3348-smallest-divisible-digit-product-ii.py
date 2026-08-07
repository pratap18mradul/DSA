class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        # Factor contribution of digits 0-9
        # Order: 2, 3, 5, 7
        factor = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        ]

        # -----------------------------------------
        # Factorize t
        # -----------------------------------------

        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i in range(4):
            p = primes[i]

            while t % p == 0:
                t //= p
                need[i] += 1

        # t contains some prime other than 2,3,5,7
        if t != 1:
            return "-1"

        # -----------------------------------------
        # Convert prime factors into minimum digits
        # -----------------------------------------

        def get_factors(c):
            c2, c3, c5, c7 = c

            # 2^3 = 8
            count8 = c2 // 3
            remaining2 = c2 % 3

            # 3^2 = 9
            count9 = c3 // 2
            count3 = c3 % 2

            # 2^2 = 4
            count4 = remaining2 // 2
            count2 = remaining2 % 2

            # 2 * 3 = 6
            count6 = 0

            if count2 == 1 and count3 == 1:
                count2 = 0
                count3 = 0
                count6 = 1

            # 3 * 4 = 2 * 6
            if count3 == 1 and count4 == 1:
                count2 = 1
                count6 = 1
                count3 = 0
                count4 = 0

            # [digit 2,3,4,5,6,7,8,9]
            return [
                count2,
                count3,
                count4,
                c5,
                count6,
                c7,
                count8,
                count9
            ]

        def build(f):
            ans = []

            for i in range(8):
                digit = i + 2
                ans.append(str(digit) * f[i])

            return ''.join(ans)

        def count(f):
            return sum(f)

        def subtract(a, b):
            return [
                max(0, a[0] - b[0]),
                max(0, a[1] - b[1]),
                max(0, a[2] - b[2]),
                max(0, a[3] - b[3])
            ]

        # -----------------------------------------
        # Minimum digits needed for t
        # -----------------------------------------

        min_factors = get_factors(need)

        # If minimum required digits are already
        # longer than num, this is automatically
        # the smallest possible answer.
        if count(min_factors) > len(num):
            return build(min_factors)

        # -----------------------------------------
        # Count prime factors in num
        # -----------------------------------------

        current = [0, 0, 0, 0]

        for ch in num:
            f = factor[ord(ch) - 48]

            current[0] += f[0]
            current[1] += f[1]
            current[2] += f[2]
            current[3] += f[3]

        # -----------------------------------------
        # If num itself is valid
        # -----------------------------------------

        first_zero = num.find('0')

        if first_zero == -1:

            if (
                current[0] >= need[0] and
                current[1] >= need[1] and
                current[2] >= need[2] and
                current[3] >= need[3]
            ):
                return num

            first_zero = len(num)

        # -----------------------------------------
        # Try changing one digit
        # from RIGHT -> LEFT
        # -----------------------------------------

        for i in range(len(num) - 1, -1, -1):

            d = ord(num[i]) - 48

            # Remove current digit's factors
            f = factor[d]

            current[0] = max(0, current[0] - f[0])
            current[1] = max(0, current[1] - f[1])
            current[2] = max(0, current[2] - f[2])
            current[3] = max(0, current[3] - f[3])

            space = len(num) - 1 - i

            # Prefix cannot contain zero
            if i > first_zero:
                continue

            # Try every bigger digit
            for bigger in range(d + 1, 10):

                # Factors still required
                remaining = subtract(need, current)

                # Remove factors supplied by bigger digit
                remaining = subtract(
                    remaining,
                    factor[bigger]
                )

                # Convert remaining factors to digits
                suffix = get_factors(remaining)

                required = count(suffix)

                # Enough space for suffix
                if required <= space:

                    ones = '1' * (space - required)

                    return (
                        num[:i]
                        + str(bigger)
                        + ones
                        + build(suffix)
                    )

        # -----------------------------------------
        # No answer with same length.
        # Need one extra digit.
        # -----------------------------------------

        min_factors = get_factors(need)

        return (
            '1' * (len(num) + 1 - count(min_factors))
            + build(min_factors)
        )