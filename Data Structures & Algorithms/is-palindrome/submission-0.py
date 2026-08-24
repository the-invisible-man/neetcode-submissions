class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        chars = list(s)

        while j > i:
            cur_i = i
            cur_j = j

            if chars[i].isalnum() is False:
                i+=1

            if chars[j].isalnum() is False:
                j-=1

            if cur_i != i or cur_j != j:
                continue

            if chars[i].lower() != chars[j].lower():
                return False

            i+=1
            j-=1

        return True
