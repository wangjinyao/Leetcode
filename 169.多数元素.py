#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
# 用投票算法，只要票数为0就取下一个值为候选人，记录1票，后续同人则+1票，不同则-1票，最终候选人就是多数元素
# 因为任何时刻票数为0都表示前面出现的候选人和其他人平票了。而多数元素不会出现平票，所以多数元素会一直坚持到最后。候选人如果不是多数，那后面肯定会被多数候选人推翻。
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        voteCount = 0
        for n in nums:
            if voteCount == 0:
                num = n
            if num == n:
                voteCount += 1
            else:
                voteCount -= 1
        return num


# @lc code=end

