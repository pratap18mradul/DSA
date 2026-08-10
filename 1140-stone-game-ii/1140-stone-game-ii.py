from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to n-1
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0

            # Can take all remaining piles
            if 2 * M >= n - i:
                return suffix[i]

            best = 0

            # Take x piles, where 1 <= x <= 2*M
            for x in range(1, 2 * M + 1):
                # Opponent gets the best possible result
                opponent = dp(i + x, max(M, x))

                # Stones Alice can secure
                best = max(best, suffix[i] - opponent)

            return best

        return dp(0, 1)