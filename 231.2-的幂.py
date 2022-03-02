#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n == 2:
            return True
        div, mod = divmod(n, 2)
        if mod:
            return False
        return self.isPowerOfTwo(div)


# @lc code=end

