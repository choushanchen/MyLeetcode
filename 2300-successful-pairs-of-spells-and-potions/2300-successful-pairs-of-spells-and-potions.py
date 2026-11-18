class Solution:        
    def lowerBound(self, nums: list[int], target) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        ans = []
        n = len(potions)
        potions.sort()
        for s in spells:
            target = (success + s - 1) // s
            i = self.lowerBound(potions, target)
            print(i)
            ans.append(n - i)
        return ans

        
        
        