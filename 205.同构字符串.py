#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        strDict = {}
        for i in range(len(s)):
            s_str = s[i]
            t_str = t[i]
            if s_str in strDict and strDict[s_str] != t_str:
                return False
            if s_str not in strDict and t_str in strDict.values():
                return False
            if s_str not in strDict and t_str not in strDict.values():
                strDict[s_str] = t_str
        else:
            return True


# @lc code=end

