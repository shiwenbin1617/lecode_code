"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

"""
from typing import List
import os


# 暴力法解题目
# class Solution:
#     def two_sum(self, nums: List[int], target: int) -> List[int]:
#         result = []
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     result = [i, j]
#         return result

# 哈希表法（官方解发）
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         harsh_table = dict()
#         for i in range(n):
#             if target - nums[i] in harsh_table:
#                 return [harsh_table[target - nums[i]],i]
#             else:
#                 harsh_table[nums[i]] = i
#         return []

# 哈希表发，自己的笨办法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        # 将数组元素加入哈希表中
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for j in range(len(nums)):
            if target - nums[j] in hash_map:
                # 判断结果是否为同一个元素,如果不等于则返回
                if hash_map[target - nums[j]] != j:
                    return [hash_map[target - nums[j]], j]


if __name__ == '__main__':
    fruit = Solution()
    kk = fruit.twoSum(nums=[3, 2,4], target=6)
    print(kk)
