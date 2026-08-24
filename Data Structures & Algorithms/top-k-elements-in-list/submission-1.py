class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        ans = []

        for n in nums:
            if n in tracker:
                tracker[n] += 1
            else:
                tracker[n] = 1

        for n, frequency in tracker.items():
            buckets[frequency].append(n)

        # visit each bucket in reverse order
        # and explore each bucketed item
        for bucket in reversed(buckets):
            for n in bucket:
                ans.append(n)

                if len(ans) == k:
                    return ans 