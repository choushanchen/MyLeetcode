class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        def lower_bound(x: int):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left 
        neg = lower_bound(0)
        pos = len(nums) - lower_bound(1)
        return max(neg, pos)
        