from collections import Counter
class Solution:
    def minArrivalsToDiscard(self, arrivals:list[int], w:int, m:int) -> int:
        ans = 0
        count = Counter()
        kept = [False] * len(arrivals)  
        for i in range(len(arrivals)):
            x = arrivals[i]
            if count[x] < m:
                count[x] += 1
                kept[i] = True
            else:
                ans += 1
            left = i - w + 1
            if left >= 0 and kept[left]:
                count[arrivals[left]] -= 1
        return ans
            
            





































'''
class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int],  w: int, m: int) -> int:

        mx, ans = max(arrivals), 0
        ctr = [0] * (mx + 1)
      
        for idx, rght in enumerate(arrivals):
            if idx >= w: 
                left = arrivals[idx - w]
                ctr[left]-= (left != 0)

            if ctr[rght] == m:
                ans+= 1
                arrivals[idx] = 0
            else:
                ctr[rght]+= 1
                
        return ans
        

from collections import Counter

class Solution:
    def minArrivalsToDiscard(self, arrivals: list[int], w: int, m: int) -> int:
        n = len(arrivals)
        counts = Counter()      # 统计当前窗口内保留的物品频次
        kept = [False] * n      # 标记第 i 个位置的物品是否被保留
        discards = 0

        for i, item in enumerate(arrivals):
            # 1. 如果窗口左侧移出界外的那个物品之前是被保留的，计数 -1
            if i >= w and kept[i - w]:
                counts[arrivals[i - w]] -= 1

            # 2. 判断当前物品能否保留
            if counts[item] < m:
                counts[item] += 1
                kept[i] = True  # 标记为保留
            else:
                discards += 1   # 超过限制，只能丢弃

        return discards
'''