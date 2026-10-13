from collections import Counter
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        ans = 0
        win_sum = 0
        count = Counter()
        left = 0
        for right in range (len(nums)):
            count[nums[right]] += 1
            win_sum += nums[right]
            while count[nums[right]] > 1:
                count[nums[left]] -= 1
                win_sum -= nums[left]
                left += 1
            ans = max(ans, win_sum)

        return ans
            

        