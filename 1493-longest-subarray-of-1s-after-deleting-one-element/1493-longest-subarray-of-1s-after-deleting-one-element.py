class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zeros = 0
        left = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans, right - left + 1)
            print( left,right, ans)
        return ans - 1