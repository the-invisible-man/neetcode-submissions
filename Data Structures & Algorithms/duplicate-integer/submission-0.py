class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}

        for n in nums:
            if n in table:
                return True

            table[n] = None

        return False