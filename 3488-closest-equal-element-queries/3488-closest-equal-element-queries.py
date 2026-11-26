from collections import defaultdict
class Solution:

    def lowerBound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        ans = []
        for q in queries:
            p = pos[nums[q]]
            if len(p) == 1:
                ans.append(-1)
                continue
            x = self.lowerBound(p, q) 
            best = len(nums)
            for j in ((x - 1), (x + 1) % len(p)):
                d = abs(p[j] - p[x])
                best = min(best, d, len(nums) - d)
            ans.append(best)
        return ans
            
            
        