"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 迭代法 从头到尾遍历
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         next1 = 0
#         result = ListNode(0)
#         cur = result
#
#         while l1 is not None or l2 is not None:
#             sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + next1
#             cur.next = ListNode(sum % 10)
#             next1 = sum // 10  # /运算符为浮点运算符， //为整数运算符
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#             cur = cur.next
#
#         if next1 != 0:
#             cur.next = ListNode(int(next1))
#
#         return result.next
#


# 递归法（官方解法）
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 如果 l1 为空，则返回 l2
        if not l1:
            return l2
        # 如果 l2 为空，则返回 l1
        if not l2:
            return l1

        # 将两个节点的值相加，并将结果赋给 l1 节点
        l1.val += l2.val
        # print(l1.val)
        # 如果相加的结果大于等于10，将十位上的数进位到下一个节点
        if l1.val >= 10:
            l1.next = self.addTwoNumbers(ListNode(l1.val // 10), l1.next)  # 创建一个新节点，节点的值为当前节点值除以10的商，作为下一个节点；继续递归
            l1.val %= 10  # 将余数（个位上的数）存储在当前节点中

        # 递归地处理下一个节点，并返回链表的头节点
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        # print("l1.next:"+str(l1.next))
        return l1


if __name__ == '__main__':
    fuirt = Solution()
    # 创建第一个链表
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_2.next = l1_3
    l1_1.next = l1_2

    # 创建第二个链表
    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_2.next = l2_3
    l2_1.next = l2_2
    res = fuirt.addTwoNumbers(l1_1, l2_1)
    # 输出结果
    while res is not None:
        print(res.val, end="")
        res = res.next
