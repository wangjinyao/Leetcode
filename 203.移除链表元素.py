#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        # 移除head
        while head and head.val == val:
            head = head.next
        # 移除head之后的元素
        point = head
        while point and point.next:
            if point.next.val == val:
                point.next = point.next.next
            else:
                point = point.next
        return head


# @lc code=end

