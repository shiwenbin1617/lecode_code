"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

# """
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         carry = 0
#         result = ""
#
#         # 首先将 a 和 b 的长度补齐
#         max_len = max(len(a), len(b))
#         a = a.zfill(max_len)
#         b = b.zfill(max_len)
#
#         for i in range(max_len - 1, -1, -1):
#             bit_sum = int(a[i]) + int(b[i]) + carry
#             if bit_sum >= 2:
#                 carry = 1
#                 bit_sum -= 2
#             else:
#                 carry = 0
#             result = str(bit_sum) + result
#
#         if carry == 1:
#             result = "1" + result
#
#         return result

class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))
