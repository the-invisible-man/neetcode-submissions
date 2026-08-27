import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        zero_index = None

        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = i
            else:
                product *= num

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            result = [0] * len(nums)
            result[zero_index] = product
            return result

        return [product // num for num in nums]
