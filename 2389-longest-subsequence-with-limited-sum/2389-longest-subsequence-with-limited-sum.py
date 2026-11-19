class Solution:

    def lowerBound(self, nums: list[int], target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        ans = []
        pre = []
        nums.sort()
        s = 0
        for x in nums:
            s += x
            pre.append(s)
        for q in queries:
            ans.append(self.lowerBound(pre, q + 1))
        return ans































# class Solution:
#     def lowerBound(self, nums: list[int], target) -> int:
#         left, right = 0, len(nums)
#         while left < right:
#             mid =  (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
            
#         return left

#     def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
#         ans = []
#         pre = []
#         nums.sort()
#         s = 0
#         for x in nums:
#             s += x
#             pre.append(s) 
#         for q in queries:
#             ans.append(self.lowerBound(pre, q + 1))
#         return ans
        

        