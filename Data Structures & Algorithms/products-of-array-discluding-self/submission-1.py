import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = set()
        product = 1
        zero_key = None

        for key, num in enumerate(nums):
            if num == 0:
                zeros.add(key)
                zero_key = key
            else:
                product = num * product

        total_zeroes = len(zeros)

        for key, num in enumerate(nums):
            if total_zeroes == 0:
                nums[key] = product // num
            elif total_zeroes == 1:
                if key == zero_key:
                    nums[zero_key] = product
                else:
                    nums[key] = 0
            else:
                nums[key] = 0

        return nums