class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        count = 0
        for right in range(len(s)):
            if right > 0 and s[right] == s[right - 1]:
                count += 1
            while count >= 2:
                if s[left] == s[left + 1]:
                    count -= 1
                left += 1 
            ans = max(ans, right - left + 1)
        return ans

































# class Solution:
#     def longestSemiRepetitiveSubstring(self, s: str) -> int:
#         ans = 0
#         sum_adj_pair = 0
#         left = 0
#         for right in range(len(s)):
#             if right > 0 and s[right] == s[right - 1]:
#                 sum_adj_pair += 1
#             while sum_adj_pair == 2:
#                 if s[left] == s[left + 1]:
#                     sum_adj_pair -= 1
#                 left += 1
#             ans = max(ans, right - left + 1)
#         return ans

        