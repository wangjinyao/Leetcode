#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
# 二分查找，注意去掉已经测试过的值
#
# #

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    result = solution.mySqrt(2)
    print(result)
