#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
# 1. 创建p，q两条分区链表的首尾变量，共四个
# 2. 遍历原始链表，如果是和前一个值位于一样的分区，则移动p或q的终点，继续遍历
# 3. 如果和前一个值不同，则将p或者q的终点指向这个值，然后移动p或q的终点，继续遍历
# 4. 遍历完成后，按照大小，将pq首尾相连，返回最起点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p_start=p_end=q_start=q_end = None
        tmp = head
        smaller = None
        while tmp:
            if tmp.val <x:
                if not p_start:
                    p_start = tmp
                
                if p_end and smaller is False:
                    p_end.next = tmp
                smaller = True
                p_end = tmp
            else:
                if not q_start:
                    q_start = tmp
                if q_end and smaller is True:
                    q_end.next = tmp
                smaller = False
                q_end = tmp
            tmp = tmp.next
        if p_end:
            p_end.next = q_start
        if q_end:
            q_end.next = None
        
        if p_start:
            return p_start
        elif q_start:
            return q_start
        else:
            return head

# @lc code=end

