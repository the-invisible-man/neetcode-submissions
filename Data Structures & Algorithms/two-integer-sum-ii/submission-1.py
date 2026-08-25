class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tracker = {}

        for key, n in enumerate(numbers):
            if n in tracker:
                return [tracker[n]+1, key+1]

            tracker[target-n] = key