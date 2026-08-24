class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        tracker = {}

        for s in strs: # n
            signature = self.signature(s)

            if signature in tracker:
                ans[tracker[signature]].append(s)
                continue

            group_index = len(ans)
            tracker[signature] = group_index

            ans.append([s])

        return ans

    def signature(self, s: str) -> str:
        key = [0] * 26

        for char in s:
            key[ord(char)-97] += 1

        return tuple(key)
