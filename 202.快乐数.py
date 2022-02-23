#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
# 只要一个数出现循环就是不是快乐数
# 不是快乐数的计算过程出现的数也都不是快乐数
# 是快乐数的就算过程出现的数也都是快乐数
# 快乐数收敛为1，则最后一定是1000形式，即平方和为整10
# 1-10的平方个位数分别为1，4，9，6，5，6，9，4，1，0
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(num):
            if num < 10:
                return num ** 2
            else:
                div, mod = divmod(num, 10)
                return squareSum(div) + mod ** 2

        sums = set()
        while True:
            n = squareSum(n)
            if n in sums:
                break
            sums.add(n)
        return 1 in sums


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    num = 123456
    ret = solution.isHappy(num)
    print(ret)
