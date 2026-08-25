class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        result = list()

        for i, n in enumerate(nums):
            j = 0
            k = len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                
                if i == j:
                    j += 1
                    continue

                if i == k:
                    k -= 1
                    continue

                if curr_sum == 0:
                    tup = (nums[i], nums[j], nums[k])
                    key = hash(tuple(sorted(tup)))

                    if key not in seen:
                        seen.add(key)
                        result.append([nums[i], nums[j], nums[k]])

                    k -= 1
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    j += 1

        return result