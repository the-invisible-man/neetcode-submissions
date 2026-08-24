class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in dict_1:
                dict_1[char] += 1
            else:
                dict_1[char] = 1

        for char in t:
            if char in dict_2:
                dict_2[char] += 1
            else:
                dict_2[char] = 1

        return dict_1 == dict_2