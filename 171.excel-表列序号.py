#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
# 仿照26进制， (ord(符号)-64)*26**n，相加即结果
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if not columnTitle:
            return 0
        else:
            num = ord(columnTitle[-1]) - 64
        return self.titleToNumber(columnTitle[:-1]) * 26 + num


# @lc code=end

