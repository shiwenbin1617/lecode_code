"""
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
"""

# 暴力法 搜索所有子串，然后判断是否为回文串
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)  # 字符串 s 的长度
#         max_len = 0  # 最长回文子串的长度
#         start, end = 0, 0  # 最长回文子串的起始和结束位置
#         for i in range(n):  # 枚举所有可能的起始位置
#             for j in range(i + 1, n + 1):  # 枚举所有可能的结束位置
#                 print(j)
#                 substr = s[i:j]  # 当前子串
#                 if substr == substr[::-1]:  # 如果当前子串是回文串
#                     if j - i > max_len:  # 如果当前回文子串的长度大于之前找到的最长回文子串的长度
#                         max_len = j - i  # 更新最长回文子串的长度
#                         start, end = i, j  # 更新最长回文子串的起始和结束位置
#         return s[start:end]  # 返回最长回文子串

# 暴力法 扩展中心字串
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2:
#             return s
#
#         def extend_palindrome(l, r):
#             while l >= 0 and r < n and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#             return s[l + 1:r]
#
#         res = ""
#         for i in range(n):
#             # 以当前字符为中心，扩展出回文子串
#             s1 = extend_palindrome(i, i)
#             s2 = extend_palindrome(i, i + 1)
#
#             # 取两种情况中更长的那一个作为当前位置的最长回文子串
#             cur_res = s1 if len(s1) > len(s2) else s2
#
#             # 更新全局最长回文子串
#             if len(cur_res) > len(res):
#                 res = cur_res
#
#         return res

# 官方解发
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2 or s == s[::-1]:  # 如果s的长度小于2或者s本身就是一个回文字符串，则直接返回s
#             return s
#         res = s[0]  # 初始化结果为s的第一个字符
#         maxlen = 1  # 初始化最长回文子串的长度为1
#         for i in range(1, len(s)):  # 从第二个字符开始遍历整个字符串
#             odd = s[i - maxlen - 1: i + 1]  # 获取以当前字符为中心的奇数长度回文子串
#             even = s[i - maxlen: i + 1]  # 获取以当前字符和前一个字符为中心的偶数长度回文子串
#             if even == even[::-1] and i - maxlen >= 0:  # 如果偶数长度回文子串是回文的，并且其长度比当前最大回文子串的长度要大，则更新最大长度和结果
#                 res = even
#                 maxlen += 1
#                 continue
#             if odd == odd[::-1] and i - maxlen - 1 >= 0:  # 如果奇数长度回文子串是回文的，并且其长度比当前最大回文子串的长度要大，则更新最大长度和结果
#                 res = odd
#                 maxlen += 2
#                 continue
#         return res  # 返回找到的最长回文子串

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # 初始化dp数组，长度为n的子串都是回文子串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        start, max_len = 0, 1  # 最长回文子串的起始位置和长度
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:  # 特殊处理长度小于等于3的子串
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        start = i
                        max_len = cur_len

        return s[start:start + max_len]


if __name__ == '__main__':
    pass