class Solution:
    def maxScore(self, cardPoints: List[int], k: int) ->int:
        win = sum(cardPoints[-k:])
        ans = win
        for i in range(k):
            win += cardPoints[i] - cardPoints[i - k]
            ans = max(ans, win)
        return ans
































# class Solution:
#     def maxScore(self, cardPoints: list[int], k: int) -> int:
#         window_score = sum(cardPoints[:k])
#         max_score = window_score
#         for i in range(k - 2, -2, -1):
#             window_score += cardPoints[i - k + 1] - cardPoints[i + 1]
#             if window_score > max_score:
#                 max_score = window_score
#         return max_score