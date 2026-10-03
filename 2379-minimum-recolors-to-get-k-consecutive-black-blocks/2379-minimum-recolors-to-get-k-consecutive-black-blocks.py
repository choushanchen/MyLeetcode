class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks) 
        window_black = blocks[:k].count('B')
        max_black = window_black
        for i in range(k, n):
            if blocks[i - k] == 'B':
                window_black -= 1
            if blocks[i] == 'B':
                window_black += 1
            if window_black > max_black:
                max_black= window_black
        return k - max_black
            
        