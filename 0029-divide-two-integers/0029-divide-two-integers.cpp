class Solution {
public:
    int divide(int dividend, int divisor) {
        // The only overflow case: -2^31 / -1 = 2^31, which doesn't fit in int
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;

        bool negative = (dividend < 0) != (divisor < 0);
        long long a = llabs((long long)dividend);
        long long b = llabs((long long)divisor);
        long long result = 0;

        while (a >= b) {
            long long temp = b, multiple = 1;
            // Double the divisor as long as it still fits into the remainder
            while (a >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            a -= temp;
            result += multiple;
        }

        return negative ? -result : result;
    }
};