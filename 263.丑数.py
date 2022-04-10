#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n in [1, 2, 3, 5]:
            return True

        for i in [2, 3, 5]:
            while True:
                div, mod = divmod(n, i)
                if div == 1 and mod == 0:
                    return True
                if mod == 0:
                    n = div
                else:
                    break
        return False


# @lc code=end

