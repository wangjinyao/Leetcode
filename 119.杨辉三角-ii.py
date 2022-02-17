#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
# 利用左右对称性质，只需要计算colIndex=rowIndex//2的值
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        preRow = self.getRow(rowIndex - 1)
        return [1] + [preRow[i] + preRow[i + 1] for i in range(rowIndex - 1)] + [1]


# @lc code=end

