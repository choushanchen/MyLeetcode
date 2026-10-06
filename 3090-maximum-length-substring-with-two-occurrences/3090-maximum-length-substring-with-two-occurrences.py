from collections import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = Counter()
        left = 0
        ans = 0
        for right,ch in enumerate(s):
            while count[ch] >= 2:
                count[s[left]] -= 1
                left += 1
            count[ch] += 1
            length = right - left + 1 
            ans = max(length,ans)
        return ans


'''
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

        