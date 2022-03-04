#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if p.val < q.val:
            minNum, maxNum = p.val, q.val
        else:
            minNum, maxNum = q.val, p.val
        if root.val > maxNum:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < minNum:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val == minNum or root.val == maxNum:
            return root
        elif minNum < root.val < maxNum:
            return root


# @lc code=end

