




from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        count = Counter(nums[:k])
        sub_count = sum(nums[:k])
        max_sub = sub_count if len(count) == k else 0
        n = len(nums)
        for i in range(k, n):
            out_sub = nums[i - k]
            count[out_sub] -= 1
            if count[out_sub] == 0:
                del count[out_sub]
            in_sub = nums[i]
            count[in_sub] += 1
            sub_count += in_sub - out_sub 
            if len(count) == k:
               max_sub = max(max_sub, sub_count)
        return max_sub

















'''
from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        ans = 0
        win_sum = sum(nums[ :k])
        count = Counter(nums[: k])
        if len(count) == k:
            ans = win_sum
        for i in range(k, len(nums)):
            win_sum += nums[i] - nums[i - k]
            count[nums[i-k]] -= 1
            if count[nums[i-k]] == 0:
                del count[nums[i - k]]
            count[nums[i]] += 1
            if len(count) == k and win_sum > ans:
                ans = win_sum
        return ans






'''


























'''
x
'''