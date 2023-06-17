"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

"""
from typing import List


# class Solution:
# def searchInsert(self, nums: List[int], target: int) -> int:
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     # 如果没有找到目标值，则返回 left，此时 left 表示目标值应该插入的位置
#     for i in range(len(nums)):
#         if nums[i] < target:
#             continue
#         else:
#             return i
#     return len(nums)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
