"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        ans = x // 2
        for i in range(1, ans + 1):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1
        return i

