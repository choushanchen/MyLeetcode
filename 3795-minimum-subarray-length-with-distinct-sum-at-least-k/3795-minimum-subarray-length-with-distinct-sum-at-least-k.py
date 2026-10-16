from collections import Counter
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        cnt = Counter()
        s = 0
        left = 0
        for right in range(len(nums)):
            x = nums[right]
            cnt[x] += 1
            if cnt[x] == 1:
                s += x
            while s >= k:
                ans = min(ans, right - left + 1)
                y = nums[left]
                cnt[y] -= 1
                if cnt[y] == 0:
                    s -= y
                left += 1
        return ans if ans != float('inf') else -1



