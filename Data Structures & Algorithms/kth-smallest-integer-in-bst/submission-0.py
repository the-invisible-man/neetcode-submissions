# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        state = [k]
        return self.helper(root, state)

    def helper(self, root: Optional[TreeNode], k: [int]) -> int|None:
        if root is None: return

        res = self.helper(root.left, k)

        if res is not None:
            return res

        if k[0] == 1:
            return root.val

        k[0] -= 1

        res = self.helper(root.right, k)

        return res
