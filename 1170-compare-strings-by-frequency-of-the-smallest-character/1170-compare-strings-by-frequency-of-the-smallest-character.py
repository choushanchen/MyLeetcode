class Solution:
    def lowerBound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right) //2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def f(self, s: list[str]) -> int:
        return  s.count(min(s))

    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        ans = []
        fw = sorted(self.f(w) for w in words)
        for q in queries:
            i = self.lowerBound(fw, self.f(q) + 1)
            ans.append(len(fw) - i)
        return ans
        