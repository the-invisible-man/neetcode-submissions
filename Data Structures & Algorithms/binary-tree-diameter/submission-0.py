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

        return longest[0] - 1

    def helper(self, root, longest: [list]):
        if root is None:
            return None

        right, left = 0, 0

        if root.right is not None:
            right = self.helper(root.right, longest)

        if root.left is not None:
            left = self.helper(root.left, longest)

        r = 1 + right + left

        if longest[0] < r:
            longest[0] = r

        return 1 + max(right, left)
