#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        #p用于遍历链表，q用于修改指向
        p = head
        q = None
        
        
        while p != None:
            q, q.next, p =p,q, p.next
        
        return q
# @lc code=end

