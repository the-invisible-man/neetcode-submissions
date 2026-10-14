class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        counter = {}
        r = 0
        l = 0

        for i in range(len(s1)):
            target[s1[i]] = target.get(s1[i], 0) + 1

        for r in range(len(s2)):
            if s2[r] not in target:
                counter = {}
                l = r + 1
                continue

            counter[s2[r]] = counter.get(s2[r], 0) + 1

            while counter[s2[r]] > target[s2[r]]:
                if s2[l] in counter:
                    counter[s2[l]] -= 1
                l += 1

            if counter == target:
                return True

        return False
