#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
# 思路：记录起始节点start，然后寻找断点，break_point表示，break_point断开连接，遍历到最后一个，连接到start

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            count+=1
        length = count

        if length<=1 or k%length==0:
            return head

        start = tmp = head
        count = 1
        break_node=None
        while tmp:
            if break_node:
                head = break_node.next
                break_node.next = None
                break_node = None

            if count == length-(k%length):
                break_node=tmp
            
            if tmp.next is None:
                tmp.next = start
                break

            tmp = tmp.next
            count +=1
        
        return head

# @lc code=end

