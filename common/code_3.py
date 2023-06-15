"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

"""


# 暴力法
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         max_len = 0
#         # 遍历整个字符串
#         for i in range(n):
#             freq = {}
#             j = i
#             # 遍历子串，如果在freq中有相同的字符就重新开始计算
#             while j < n and s[j] not in freq:
#                 freq[s[j]] = 1
#                 print(freq)
#                 print(max_len)
#                 j += 1
#             max_len = max(max_len, j - i)
#
#         return max_len

# 滑动窗格
class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        left, right = 0, 0
        max_len = 0
        char_set = set()
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                max_len = max(max_len, len(char_set))
                print(str(char_set)+"r")
            else:
                char_set.remove(s[left])
                print(str(char_set)+"    l")
                left += 1
        return max_len


if __name__ == '__main__':
    fuirt = Solution()
    kk = fuirt.lengthOfLongestSubstring("pwwkew")
    print(kk)
