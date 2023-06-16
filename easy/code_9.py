"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         if s == s[:: -1]:
#             return True
#         else:
#             return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10


# if __name__ == '__main__':
#     fuirt = Solution()
#     kk = fuirt.isPalindrome(121)
#     print(kk)
