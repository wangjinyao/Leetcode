#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# 官方天才思路：双指针，分别遍历：链表A不同部分+链表B不同部分+相同部分，则一定能遍历完或者同时到达相交节点
# 方式是双指针同步遍历，到达末尾后同时到对方头部，继续遍历，出现相同节点则是相交节点

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        if not pA or not pB:
            return None
        while pA != pB:
            if pA:
                pA = pA.next
            else:
                pA = headB
            if pB:
                pB = pB.next
            else:
                pB = headA
        return pA


# @lc code=end

