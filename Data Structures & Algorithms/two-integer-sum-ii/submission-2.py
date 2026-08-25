class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        curr_sum = numbers[p1] + numbers[p2]

        while curr_sum != target:
            if curr_sum > target:
                p2 -= 1
            else:
                p1 +=1

            curr_sum = numbers[p1] + numbers[p2]

        return [p1+1, p2+1]