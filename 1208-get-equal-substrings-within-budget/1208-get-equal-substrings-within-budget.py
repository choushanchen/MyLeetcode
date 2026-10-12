class Solution:
    def equalSubstring(self, s:str, t:str, maxCost:int) ->int:
        ans = 0
        left = 0
        cost = 0
        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans
































# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         ans = 0
#         left = 0
#         cost = 0
#         # diff = abs(ord(char1) - ord(char2))
#         for right,ch in enumerate(s):
#             diff = abs(ord(s[right]) - ord(t[right]))
#             cost += diff
#             leng = right - left
#             while cost < maxCost and leng > ans:
#                 ans = leng
#             left += 1
#         return ans
# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         ans = 0
#         left = 0
#         cost = 0
#         for right in range(len(s)):
#             cost += abs(ord(s[right]) - ord(t[right]))   # 1. 右边的字符进入窗口
#             while cost > maxCost:                         # 2. 窗口不合法，就收缩左边
#                 cost -= abs(ord(s[left]) - ord(t[left]))
#                 left += 1
#             ans = max(ans, right - left + 1)              # 3. 窗口已合法，更新答案
#         return ans       