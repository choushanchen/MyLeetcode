class Solution:
     def longestSubarray(self, nums: list[int]) -> int:
        ans = 0
        left = 0
        z = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                z += 1
            while z == 2:
                if nums[left] == 0:
                    z -= 1
                left += 1
            ans = max(ans, right - left)
        return ans



































# class Solution:
#     def longestSubarray(self, nums: list[int]) -> int:
#         zeros = 0
#         left = 0 
#         ans = 0
#         for right,num in enumerate(nums):
#             if num == 0:
#                 zeros += 1
#             while zeros > 1:
#                 if nums[left] == 0:
#                     zeros -= 1
#                 left += 1
#             ans = max(ans, right - left)
#         return ans


'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        ans = 0
        for right,ch in enumerate(s):
            while ch in chars:
                chars.remove(s[left])
                left += 1
            chars.add(ch)
            length = right - left + 1
            ans = max(length, ans)
        return ans
'''