"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1 。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。

"""


# class Solution:
#
#     SYMBOL_VALUES = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000,
#     }
#
#     def romanToInt(self, s: str) -> int:
#         ans = 0
#         n = len(s)
#         for i, ch in enumerate(s):
#             value = Solution.SYMBOL_VALUES[ch]
#             if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
#                 ans -= value
#             else:
#                 ans += value
#         return ans

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if s[i] not in values:
                raise ValueError("Invalid Roman numeral")
            if i > 0 and values[s[i]] > values[s[i - 1]]:
                result += values[s[i]] - 2 * values[s[i - 1]]
            else:
                result += values[s[i]]
            print(values[s[i]])
            print(2 * values[s[i - 1]])
            print(result)
        return result


if __name__ == '__main__':
    fuirt = Solution()
    kk = fuirt.romanToInt("IV")
    # print(kk)