class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        tracker = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s in tracker:
                ans[tracker[sorted_s]].append(s)
                continue

            group_index = len(ans)
            tracker[sorted_s] = group_index

            ans.append([s])

        return ans