class Solution:
    def trap(self, heights: List[int]) -> int:
        max_left_height = 0
        max_right_height = 0
        i = 0
        j = len(heights) - 1
        max_left = {}
        max_right = {}
        result = 0

        while i < len(heights):
            max_left[i] = max_left_height
            max_right[j] = max_right_height

            # Is this a new max height?
            if heights[i] > max_left_height:
                max_left_height = heights[i]

            if heights[j] > max_right_height:
                max_right_height = heights[j]

            i += 1
            j -= 1

        for key, num in enumerate(heights):
            total = min(max_left[key], max_right[key]) - heights[key]

            if total > 0:
                result += total

        return result
        
            