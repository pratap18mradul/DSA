from bisect import bisect_right

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # Store all positions of every character in word1
        pos = {}

        for i, ch in enumerate(word1):
            if ch not in pos:
                pos[ch] = []
            pos[ch].append(i)

        # right0[j]:
        # Latest possible index where word2[j] can start
        # if the rest must match EXACTLY.
        right0 = [-1] * (m + 1)

        # right1[j]:
        # Latest possible index where word2[j] can start
        # with AT MOST ONE mismatch.
        right1 = [-1] * (m + 1)

        # Empty suffix can always be matched
        right0[m] = n
        right1[m] = n

        # Build from right to left
        for j in range(m - 1, -1, -1):
            ch = word2[j]

            # -------------------------
            # Exact match
            # -------------------------
            limit = right0[j + 1] - 1

            if limit >= 0 and ch in pos:
                k = bisect_right(pos[ch], limit) - 1

                if k >= 0:
                    right0[j] = pos[ch][k]

            # -------------------------
            # At most one mismatch
            # -------------------------

            # Option 1: current character matches
            limit = right1[j + 1] - 1
            match = -1

            if limit >= 0 and ch in pos:
                k = bisect_right(pos[ch], limit) - 1

                if k >= 0:
                    match = pos[ch][k]

            # Option 2: use our one mismatch here
            limit = right0[j + 1] - 1
            mismatch = -1

            if limit >= 0:
                if word1[limit] != ch:
                    mismatch = limit
                else:
                    mismatch = limit - 1

            right1[j] = max(match, mismatch)

        # No valid sequence
        if right1[0] == -1:
            return []

        # --------------------------------
        # Greedily build lexicographically
        # smallest index sequence
        # --------------------------------

        ans = []

        prev = -1
        used_mismatch = False

        for j in range(m):
            ch = word2[j]

            i = prev + 1

            while i < n:

                # Case 1: characters match
                if word1[i] == ch:

                    if used_mismatch:
                        possible = right0[j + 1] > i
                    else:
                        possible = right1[j + 1] > i

                # Case 2: characters don't match
                else:

                    # We can only use mismatch once
                    if not used_mismatch:
                        possible = right0[j + 1] > i
                    else:
                        possible = False

                if possible:
                    ans.append(i)

                    if word1[i] != ch:
                        used_mismatch = True

                    prev = i
                    break

                i += 1

        return ans