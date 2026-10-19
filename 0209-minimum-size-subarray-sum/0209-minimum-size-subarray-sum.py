class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]):
        ans = float("inf")
        s = 0
        left = 0
        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans != float("inf") else 0
































# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]):
#         ans = float('inf')
#         left = 0
#         count = 0
#         for right in range(len(nums)):
#             count += nums[right]
#             while count >= target:
#                 ans = min(ans, right - left + 1)
#                 count -= nums[left]
#                 left += 1
#         return ans if ans != float('inf') else 0

# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         ans = float('inf')
#         left = 0
#         count = 0 
#         for right in range(len(nums)):
#             count += nums[right]
#             while count >= target:
#                 ans = min(ans, right - left + 1)
#                 count -= nums[left]
#                 left += 1
#         return ans if ans != float('inf') else 0               
        