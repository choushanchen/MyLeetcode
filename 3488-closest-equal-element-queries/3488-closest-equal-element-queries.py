from collections import defaultdict

class Solution:
    def lowerBound(self, nums: list[int], target: int) -> int:
        right, left = len(nums), 0
        while left < right:
            mid = (left + right) //2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i,x in enumerate(nums):
            pos[x].append(i)
        ans = []
        for q in queries:
            p = pos[nums[q]]
            i = self.lowerBound(p, q)
            if len(p) == 1:
                ans.append(-1)
                continue
            best = len(nums)                          # 任何距离都比它小
            for j in (p[i - 1], p[(i + 1) % len(p)]): # 左邻居、右邻居
                d = abs(q - j)                        # 直走
                best = min(best, d, len(nums) - d)    # 和绕圈比，取最小
            ans.append(best)
        return ans                                    # 注意缩进：在 for 外面


            #I know there's still a part to compare the neighbourhood I forget its code.



        