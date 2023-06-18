"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         a = b = 1
#         for i in range(2, n + 1):
#             a, b = b, a + b
#         return b

class Solution:
    def climbStairs(self, n: int) -> int:
        s = [1, 2]
        if n <= 2:
            return s[n - 1]
        while len(s) < n:
            s.append(s[-1] + s[-2])
            print(s)
        return s[-1]


if __name__ == '__main__':
    fuirt = Solution()
    kk = fuirt.climbStairs(10)
    print(kk)
