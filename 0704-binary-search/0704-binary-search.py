class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if left < len(nums) and nums[left] == target else -1































# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         left, right = 0, len(nums)
#         while left < right:
#             mid = (right + left)//2
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left if left < len(nums) and nums[left] == target else -1
    

        