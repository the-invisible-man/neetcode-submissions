class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        deduped = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in deduped:
                length = 0
                while (n + length) in deduped:
                    length += 1

                longest = max(length, longest)

        return longest