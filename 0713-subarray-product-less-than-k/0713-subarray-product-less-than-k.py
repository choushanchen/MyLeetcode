class Solution:
    def numSubarrayProductLessThanK(self, nums:List[int], k:int) -> int:
        ans = 0
        prod = 1
        left = 0
        if k <= prod:
            return ans
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans






























# class Solution:
#     def numSubarrayProductLessThanK(self, nums:List[int], k:int) -> int:
#         ans = 0
#         left = 0
#         prod = 1
#         if k <= prod:
#             return ans
#         for right in range(len(nums)):
#             prod *= nums[right]
#             while prod >= k:
#                 prod //= nums[left]
#                 left += 1
#             ans += right - left + 1
#         return ans




# class Solution:
#     def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
#         if k <= 1:
#             return 0
#         ans = 0
#         prod = 1
#         left = 0
#         for right in range(len(nums)):
#             prod *= nums[right]
#             while prod >= k:
#                 prod //= nums[left]
#                 left += 1
#             ans += right - left + 1
#         return ans

"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # State: prod = product of nums[left..right]
        # Invalid: prod >= k
        # Answer: after shrinking, add right - left + 1
        if k <= 1:
            return 0
        ans = 0
        prod = 1
        left = 0
        for right in range(len(nums)):
            prod *= nums[right]             # enter
            while prod >= k:                # shrink while invalid
                prod //= nums[left]         # leave
                left += 1
            ans += right - left + 1         # count subarrays ending at right
        return ans
"""
                   
                




