from collections import defaultdict

class Solution:
    def lowerBound(self, nums: List[int], target)-> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i,x in enumerate(nums):
            pos[x].append(i)
        ans = []
        for q in queries:
            p = pos[nums[q]]
            if len(p) == 1:
                ans.append(-1)
                continue
            k = self.lowerBound(p, q)
            best = n
            for j in (p[k - 1], p[(k + 1) % len(p)]):
                d = abs(q - j)
                best = min(best,d, n-d)
            ans.append(best)
        return ans
        