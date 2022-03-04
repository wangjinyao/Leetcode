#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        mod = num % 9
        if mod == 0:
            return 9
        else:
            return mod


# @lc code=end

