# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')

        def max_sum(node: TreeNode) -> int:
            if not node:
                return 0
            left_sum = max(max_sum(node.left),0)
            right_sum = max(max_sum(node.right),0)
            self.best = max(self.best,left_sum+right_sum + node.val)
            return node.val + max(left_sum,right_sum)
        max_sum(root)
        return self.best