class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        counter = 0
        ans = []

        for n in nums:
            compliment = target - n

            # Check if the compliment exists
            if compliment in tracker:
                ans = [tracker[compliment], counter]
                break

            # Track this value
            tracker[n] = counter

            counter += 1

        return ans
