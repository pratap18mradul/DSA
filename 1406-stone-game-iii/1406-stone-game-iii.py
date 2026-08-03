class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # dp[i] = maximum score difference
        # (current player - other player) from index i
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float("-inf")
            total = 0

            # Take 1, 2, or 3 stones
            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]

                # Current player's gain - opponent's best difference
                dp[i] = max(dp[i], total - dp[j + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"