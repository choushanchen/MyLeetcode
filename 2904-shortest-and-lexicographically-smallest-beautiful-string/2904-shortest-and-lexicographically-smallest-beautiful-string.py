class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        ones = 0
        left = 0
        for right in range(len(s)):
            if s[right] == "1":
                ones += 1
            while ones >= k:
                t = s[left:right + 1]
                if ans == "" or (len(t), t) < (len(ans), ans):
                    ans = t
                if s[left] == "1":
                    ones -= 1
                left += 1
        return ans 
# class Solution:
#     def shortestBeautifulSubstring(self, s: str, k: int) -> str:
#         ans = ""
#         left = 0
#         ones = 0
#         for right in range(len(s)):
#             if s[right] == "1":
#                 ones += 1
#             while ones > k:
#                 if s[left] == "1":
#                     ones -= 1
#                 left += 1
#             if ones == k:
#                 while s[left] == "0":
#                     left += 1
#                 t = s[left:right + 1]
#                 if ans == "" or (len(t), t) < (len(ans), ans):
#                     ans = t
#         return ans
            
            

        