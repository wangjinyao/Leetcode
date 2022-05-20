#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
# 思路：设计一种哈希算法，单词字母排序后记录字母和频次，如hello→ e1h1l2o1，然后遍历数组，对单词分别哈希归类，用字典存储，key为哈希值，value为列表，最终将字典转为列表输出。
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def str_hash(word):
            result = []
            count = 0
            for char in sorted(word):
                if not result or  char != result[-1]:
                    result.append(str(count))
                    result.append(char)
                    count = 1
                else:
                    count += 1
            result.append(str(count))
            return ''.join(result)
        words = {}
        for word in strs:
            key = str_hash(word)
            if key in words:
                words[key].append(word)
            else:
                words[key] = [word]
        return list(words.values())
    
# @lc code=end

