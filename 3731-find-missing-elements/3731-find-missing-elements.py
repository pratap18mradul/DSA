class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)

        smallest = min(nums)
        largest = max(nums)

        ans = []

        for i in range(smallest, largest + 1):
            if i not in nums_set:
                ans.append(i)

        return ans