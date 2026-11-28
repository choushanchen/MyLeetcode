class Solution:
    def lowerBound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
        
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        arr2.sort()
        for i in arr1:
            minimum = self.lowerBound(arr2, i - d + 1)
            maximum = self.lowerBound(arr2, i + d + 1)
            
            if minimum == maximum:
                ans += 1
            
        return ans
        