class Solution:

    def lowerBound(self, nums: list[int], target: int, lo: int) -> int:
        left, right = lo, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            start = self.lowerBound(nums, lower - x, i + 1)      # 第一个 >= lower - x
            end = self.lowerBound(nums, upper - x + 1, i + 1)    # 第一个 >  upper - x
            ans += end - start
        return ans