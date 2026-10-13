from collections import Counter
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        ans = 0
        left = 0
        count = Counter()
        for right in range(len(nums)):
            count[nums[right]] += 1
            while count[0] > k:
                count[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans