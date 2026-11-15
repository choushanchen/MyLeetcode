
def lower_bound(nums: list[int], target: int):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right)//2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for x in arr1:
            i = lower_bound(arr2, x-d)
            if i == len(arr2) or arr2[i] > x + d:
                ans += 1
        return ans
            
        



         
        