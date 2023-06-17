"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

"""
import string


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        first, ending = False, False
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] in string.ascii_lowercase + string.ascii_uppercase and ending is False:
                first = True
                count += 1

            elif s[i] not in string.ascii_lowercase + string.ascii_uppercase and first is True:
                break

        return count
