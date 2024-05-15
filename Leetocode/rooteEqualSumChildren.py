# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        root_value = root.val
        left_child = root.left.val
        right_child = root.right.val

        return left_child + right_child  == root_value