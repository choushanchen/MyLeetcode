class Solution:
    def lowerBound(self, nums: list[int], target) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def f(self, s: str) -> int:
        return s.count(min(s))

    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        fw = sorted(self.f(w) for w in words)
        n = len(fw)
        ans = []
        for q in queries:
            i = self.lowerBound(fw, self.f(q) + 1)  # 第一个 > f(q) 的位置
            ans.append(n - i)                       # 右边那一段的个数
        return ans












































# class Solution:
#     def lowerBound(self, nums: list[str], target) -> int:
#         left, right = 0, len(nums)
#         while left < right:
#             mid = (left+right)//2
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left

#     def f(self, s: str) -> int:
#         return s.count(min(s))
        
#     def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
#         fw = sorted(self.f(w) for w in words)
#         n = len(fw)
#         ans = []
#         for q in queries:
#             i = self.lowerBound(fw, self.f(q) + 1)  # 第一个 > f(q) 的位置
#             ans.append(n - i)                       # 右边那一段的个数
#         return ans


        