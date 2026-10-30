# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        state = [float("-inf")]
        res = self.helper(root, state)

        return max(res, state[0])
        
    def helper(self, root: Optional[TreeNode], state: list[int]) -> int:
        if root is None:
            return 0

        left = self.helper(root.left, state)
        right = self.helper(root.right, state)

        left, right = max(0, left), max(0, right)

        current = left + right + root.val

        state[0] = max(state[0], current, root.val)

        return max(
            left + root.val,
            right + root.val,
        )
