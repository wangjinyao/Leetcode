#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        if not paths:
            return [str(root.val)]
        return [f"{root.val}->{path}" for path in paths]


# @lc code=end
