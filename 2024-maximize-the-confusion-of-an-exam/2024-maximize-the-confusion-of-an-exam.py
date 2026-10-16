from collections import Counter
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        count = Counter()
        left = 0
        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            while count["T"] > k and count["F"] > k:
                count[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans





























# from collections import Counter
# class Solution:
#     def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
#         ans = 0
#         left = 0
#         count = Counter()
#         for right in range(len(answerKey)):
#             count[answerKey[right]] += 1
#             while (count['T'] > k) and (count['F'] > k):
#                 count[answerKey[left]] -= 1
#                 left += 1
#             ans = max(ans, right - left + 1)
#         return ans
        