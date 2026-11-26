from collections import defaultdict

class RangeFreqQuery:
    def lowerBound(self, nums: list(int), target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left 

    def __init__(self, arr: list[int]):
        self.pos = defaultdict(list)
        for i, x in enumerate(arr):
            self.pos[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        p = self.pos[value]
        start = self.lowerBound(p, left)
        end = self.lowerBound(p, right + 1)
        return end - start
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)