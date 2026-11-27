class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = len(nums1) - 1

        # insert at the end of the array
        for val in nums2:
            nums1[end] = val
            end -= 1

        # swap until in the correct order for each n value
        for i in range(n):
            current = len(nums1) - n

            for j in range(current, 0, -1):
                if nums1[j] < nums1[j-1]:
                    temp = nums1[j-1]
                    nums1[j-1] = nums1[j]
                    nums1[j] = temp
                else:
                    break

            n -= 1