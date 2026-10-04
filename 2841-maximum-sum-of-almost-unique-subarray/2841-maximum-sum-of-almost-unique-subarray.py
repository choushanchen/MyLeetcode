'''My solution——it's slow
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        count = 0
        sub_num = nums[:k]
        dist_sub = len(set(sub_num))
        if dist_sub >= m:
            count = sum(sub_num[:k])
        for i in range(1, len(nums) - k + 1):
            sub_num = nums[i: k+i]
            dist_sub = len(set(sub_num))
            if dist_sub >= m and sum(sub_num[:k]) > count:
                count = sum(sub_num[:k])
        return count
    

'''
from collections import Counter
from typing import List


class Solution:

  def maxSum(self, nums: List[int], m: int, k: int) -> int:
    # 1. 维护当前窗口内的元素频次哈希表，以及当前窗口的元素和
    count = Counter(nums[:k])
    current_sum = sum(nums[:k])

    max_sum = 0
    # 检查初始窗口是否满足不同元素数量 >= m
    if len(count) >= m:
      max_sum = current_sum

    # 2. 滑动窗口：向右移动右边界
    for i in range(k, len(nums)):
      # 移除滑动离开的左端元素 nums[i - k]
      out_num = nums[i - k]
      count[out_num] -= 1
      if count[out_num] == 0:
        del count[out_num]  # 减到 0 时删除键，保证 len(count) 正确反映不同元素个数

      # 加入新进入的右端元素 nums[i]
      in_num = nums[i]
      count[in_num] += 1

      # 增量更新窗口和
      current_sum += in_num - out_num

      # 判断当前窗口是否满足条件，更新最大和
      if len(count) >= m:
        max_sum = max(max_sum, current_sum)

    return max_sum
   