# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = [0]

        self.helper(root, longest)

        return longest[0]

    def helper(self, root, longest: list[int]):
        if root is None:
            return 0

        right = self.helper(root.right, longest)
        left = self.helper(root.left, longest)

        longest[0] = max(longest[0], right + left)

        return 1 + max(right, left)
