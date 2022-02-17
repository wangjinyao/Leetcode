#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# 思路：深度优先搜索，并自顶向下减数值，数值为零且在叶子节点则返回true

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        childrenSum = targetSum - root.val
        if not root.left and not root.right:
            # 叶子节点
            if childrenSum == 0:
                return True
            else:
                return False
        if self.hasPathSum(root.left, childrenSum) or self.hasPathSum(
            root.right, childrenSum
        ):
            return True
        else:
            return False


# @lc code=end

