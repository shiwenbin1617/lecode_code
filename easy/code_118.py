"""

"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 初始化结果数组
        result = [[1] * (i + 1) for i in range(numRows)]

        # 填充每一行的值
        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

        return result[:numRows]