#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        ran = ""
        for num in nums:
            if ran == "":
                ran += str(num)
            elif pre == num - 1:
                if ran[-1] != ">":
                    ran += "->"
            else:
                if ran[-1] == ">":
                    ran += str(pre)
                result.append(ran)
                ran = str(num)
            pre = num
        if ran[-1] == ">":
            ran += str(pre)
        result.append(ran)
        return result


# @lc code=end

