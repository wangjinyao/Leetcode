#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
# 26个字母，表示26进制，除26，余数为当前位，商继续除，获取更高位
# 相比26进制，A-Z表示的不是0-25 而是 1-26，所以对商-1。如26表示为Z
# 26个大写字母，表示chr(n+65), 如chr(1+65)=A

# @lc code=start


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        div, mod = divmod(columnNumber - 1, 26)
        if div == 0:
            return chr(65 + mod)
        else:
            return self.convertToTitle(div) + chr(65 + mod)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ret = solution.convertToTitle(52)
    print(ret)
