#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
# 思路：类比十进制规则，按位相加，然后进位。 0+0=0，0+1=1，1+1=0并进位1
# 处理顺序从最末位开始，向左处理
# 加快处理，是否进位可以通过与运算，留下的值是否为1可以通过异或运算。
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    result = solution.addBinary("11", "1")
    print(f"result={result}")
