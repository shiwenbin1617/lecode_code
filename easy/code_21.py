"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 检查两个链表是否都存在
        if l1 and l2:
            # 如果 l1 的第一个节点的值大于 l2 的第一个节点的值，则交换两个链表
            if l1.val > l2.val: l1, l2 = l2, l1
            # 递归地合并剩余的 l1 和 l2 节点
            l1.next = self.mergeTwoLists(l1.next, l2)
        # 返回非空的链表
        return l1 or l2

