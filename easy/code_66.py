"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

"""
from typing import List

from typing import List


#
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         n = len(digits)
#         for i in range(n-1, -1, -1):
#             if digits[i] != 9:
#                 digits[i] += 1
#                 for j in range(i+1, n):
#                     digits[j] = 0
#                 return digits
#
#         return [1] + [0] * n

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        l = []
        for i in digits:
            s = s + str(i)  # 全部转换成字符串
        for n in str(int(s) + 1):  # 字符串转换成int类型然后+1，再遍历字符串 添加到数组
            l.append(int(n))
        return l
