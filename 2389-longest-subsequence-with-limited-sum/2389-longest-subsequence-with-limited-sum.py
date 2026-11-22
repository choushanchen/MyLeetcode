class Solution:
    def lowerBound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        pre = [] 
        nums.sort()
        s = 0
        for n in nums:
            s += n
            pre.append(s)
        ans = []
        for q in queries:
            i = self.lowerBound(pre, q)
            ans.append(i)
        return ans
