class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        subStr = set()

        for r in range(len(s)):
            while s[r] in subStr:
                subStr.remove(s[l])
                l += 1
            subStr.add(s[r])
            longest = max(longest, r - l + 1)

        return longest