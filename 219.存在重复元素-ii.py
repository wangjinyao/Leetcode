#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
# 思路：一次遍历，队列缓存k个元素，检查当前元素是否在队列中
from typing import List

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        cache = set()
        for i in range(0, len(nums) - 1):
            cache.add(nums[i])
            if i >= k:
                cache.remove(nums[i - k])
            if nums[i + 1] in cache:
                return True
        return False


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    ret = solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
    print(ret)
