from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.cur = 0                       # 当前快照编号
        self.times = defaultdict(list)     # 每个位置：在哪些时间改过
        self.vals = defaultdict(list)      # 每个位置：改成了什么
        

    def set(self, index: int, val: int) -> None:
        self.times[index].append(self.cur) # 记一笔：什么时间
        self.vals[index].append(val)       # 改成几
        

    def snap(self) -> int:
        self.cur += 1
        return self.cur - 1                # 返回刚拍的那张的编号

    def get(self, index: int, snap_id: int) -> int:
        t = self.times[index]
        j = self.lowerBound(t, snap_id + 1) - 1   # 最后一个 ≤ snap_id 的下标
        if j < 0:                          # 从来没改过
            return 0
        return self.vals[index][j]

    def lowerBound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)