#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
# 1. 创建前置节点，从前置节点开始遍历，用pre记录上一次节点
# 2. 遇到left位置，记录为right_src节点，pre记录为left_src便于未来连线
# 3. 继续遍历，在left到right区间内，cur指向pre
# 4. 遇到right位置，记录为left_dst节点，next记录为right_dst
# 5. 遍历完后对left_srt\left_dst\right_src\right_dst连线，返回前置节点的下一个即可
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        start = ListNode()
        start.next = head
        count = 0
        cur = start
        pre = None
        right_src = right_dst = left_src = left_dst = None
        while cur:
            if count == left -1:
                right_src = cur.next
                left_src = cur
            if count == right:
                left_dst = cur
                right_dst = cur.next
            
            if count<=left:
                pre = cur
                cur = cur.next
                count+=1
            elif count<=right:
                next = cur.next
                cur.next =pre
                pre = cur
                cur = next
                count+=1
            else:
                break
        
        right_src.next=right_dst
        left_src.next=left_dst
        return start.next


# @lc code=end

