# from collections import Counter
# class Solution:
#     def lengthOfLongestSubstring(self, s:str):
#         ans = 0
#         left = 0
#         count = Counter()
#         for right in range(len(s)):
#             count[s[right]] += 1
#             while count[s[right]] > 1:
#                 count[s[left]] -= 1
#                 left += 1
#             ans = max(ans, right - left + 1)
#         return ans
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
        