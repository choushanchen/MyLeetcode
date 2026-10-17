class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ws = 0
        ans = float("inf")
        for i in range(len(blocks)):
            if blocks[i] == "W":
                ws += 1
            if i < k - 1:
                continue
            ans = min(ans, ws)
            if blocks[i-k+1] == "W":
                ws -= 1
        return ans 
            
                

































# class Solution:
#     def minimumRecolors(self, blocks: str, k: int) -> int:
#         n = len(blocks) 
#         window_black = blocks[:k].count('B')
#         max_black = window_black
#         for i in range(k, n):
#             if blocks[i - k] == 'B':
#                 window_black -= 1
#             if blocks[i] == 'B':
#                 window_black += 1
#             if window_black > max_black:
#                 max_black= window_black
#         return k - max_black
            
        