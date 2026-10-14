class Solution:
    def isValid(self, s: str) -> bool:
        closedP = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        openP = {'(', '{', '['}

        stack = []

        for c in s:
            if c in openP:
                stack.append(c)
            elif c in closedP:
                if len(stack) > 0 and closedP[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0
