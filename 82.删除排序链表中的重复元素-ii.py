#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
# 思路：
# 1. 创建前置节点，从前置节点开始遍历
# 2. 如果当前节点值等于重复值，则看下一个节点
# 3. 如果当前节点值不等于重复值，且下一节点值不等于当前节点值，则将前置节点指向当前节点，当前节点变为前置节点
# 4. 如果当前节点值不等于重复值，但下一节点值等于当前节点值，则记录重复值，并看下一个节点
# 5. 遍历直至当前节点为空，然后返回最开始节点的下个节点
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = pre = ListNode()

        dup_val = None
        tmp = head
        while tmp:
            if tmp.val == dup_val:
                tmp = tmp.next
            elif tmp.next and tmp.next.val==tmp.val:
                dup_val = tmp.val
                tmp = tmp.next.next
            else:
                pre.next = tmp
                pre = tmp
                tmp = tmp.next
        pre.next = None
        return start.next
# @lc code=end

