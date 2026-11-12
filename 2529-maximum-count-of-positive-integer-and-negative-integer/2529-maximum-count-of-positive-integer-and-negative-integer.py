class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        left, right = 0, len(nums)
        zeros = sum(1 for x in nums if x == 0)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid
        return left if left > len(nums) - left - zeros else len(nums) - left - zeros

        