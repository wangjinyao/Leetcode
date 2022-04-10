#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split(" ")
        strdict = {}
        if len(pattern) != len(strs):
            return False
        for i, char in enumerate(pattern):
            if char in strdict:
                if strdict[char] != strs[i]:
                    return False
            elif strs[i] in strdict.values():
                return False
            else:
                strdict[char] = strs[i]

        return True


# @lc code=end

