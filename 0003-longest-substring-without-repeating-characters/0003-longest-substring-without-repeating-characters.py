from collections import Counter 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        count = Counter()
        for right in range(0, len(s)):
            count[s[right]] += 1
            while count[s[right]] > 1:
                count[s[left]] -= 1 
                left += 1
            ans = max(ans, right - left + 1)
        return ans
