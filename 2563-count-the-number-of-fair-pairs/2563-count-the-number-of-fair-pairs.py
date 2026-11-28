class Solution:
    def lowerBound(self, nums: list[int], target: int, lo: int) -> int:
        left, right = lo, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left 

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            start = self.lowerBound(nums, lower - nums[i], i + 1)
            end = self.lowerBound(nums, upper - nums[i] + 1, start)
            ans += end - start 
            print(i,start, end,ans)
        return ans
        