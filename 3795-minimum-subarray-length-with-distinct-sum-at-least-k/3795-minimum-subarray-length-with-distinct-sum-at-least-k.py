from collections import Counter
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        left = 0
        s = 0
        ans = float('inf')
        for right in range(len(nums)):
            r = nums[right]
            cnt[r] += 1
            if cnt[r] == 1:
                s += r
            while s >= k:
                ans = min(ans, right - left + 1)
                l = nums[left]
                if cnt[l] == 1:
                    s -= l
                cnt[l] -= 1
                left += 1
        return ans if ans != float('inf') else -1

# from collections import Counter
# class Solution:
#     def minLength(self, nums: List[int], k: int) -> int:
#         ans = float("inf")
#         left = 0
#         cnt = Counter()
#         s = 0
#         for right in range(len(nums)):
#             cnt[nums[right]] += 1
#             if cnt[nums[right]] == 1:
#                 s += nums[right]
#             while s >= k:
#                 ans = min(ans, right - left + 1)
#                 cnt[nums[left]] -= 1
#                 if cnt[nums[left]] == 0:
#                     s -= nums[left]
#                     del cnt[nums[left]]
#                 left += 1
#         return ans if ans != float("inf") else -1

# from collections import Counter
# class Solution:
#     def minLength(self, nums: List[int], k: int) -> int:
#         ans = float('inf')
#         cnt = Counter()
#         s = 0
#         left = 0
#         for right in range(len(nums)):
#             r = nums[right]
#             cnt[r] += 1
#             if cnt[r] == 1:
#                 s += r
#             while s >= k:
#                 ans = min(ans, right - left + 1)
#                 l = nums[left]
#                 cnt[l] -= 1
#                 if cnt[l] == 0:
#                     s -= l
#                 left += 1
#         return ans if ans != float('inf') else -1



