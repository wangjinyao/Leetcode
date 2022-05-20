# 2. 给定一个奇数位升序，偶数位降序的单链表，编写一个函数，将其按照升序进行排序
# 输入: 1->8->3->6->5->4->7->2->NULL
# 输出: 1->2->3->4->5->6->7->8->NULL


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def show_val(head):

    current = head
    while current:
        print(current.val,end='->')
        current = current.next
    print('NULL')

def solution(head):
    # 拆分成两个链表
    current = head
    a = head
    b = None
    last = None
    while current:
        if not b and last:
            b = current
        if last:
            last.next = current.next
        last = current
        current = current.next
    if last:
        last.next = None
    show_val(a)
    show_val(b)
    # 对偶数位链表倒序
    current = b
    last = None
    while current:
        last, last.next, current = current, last, current.next
    b = last
    show_val(a)
    show_val(b)
    # 合并链表
    last = result = Node()
    while a and b:
        # print(a.val, b.val)
        if a.val <= b.val:
            last.next = a
            last = a
            a = a.next
            
        else:
            last.next = b
            last = b
            b = b.next
            
    # show_val(result)
    while a:
        last.next = a
        last = a
        a = a.next

    while b:
        last.next = b
        last = b
        b = b.next


    head = result.next
    return head

if __name__=='__main__':
    # 1->8->3->6->5->4->7->2->NULL
    tmp = [1,8,3,6,5,4,7,2,9]
    last = None
    for x in tmp[::-1]:
        node = Node(x, last)
        last = node
    head = last
    show_val(head)


    result = solution(head)

    # 输出
    show_val(head)
