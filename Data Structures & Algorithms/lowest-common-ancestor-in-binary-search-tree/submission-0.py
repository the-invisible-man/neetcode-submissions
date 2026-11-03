# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while True:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif q.val < cur.val and p.val < cur.val:
                cur = cur.left
            else:
                return cur

                