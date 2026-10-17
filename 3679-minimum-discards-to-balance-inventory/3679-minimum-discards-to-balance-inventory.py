from collections import Counter
class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int,m: int) -> int:
        left = 0
        cnt = Counter()
        discard = 0
        n = len(arrivals) 
        kept = [False] * n
        for right in range(n):
            if right >= w:
                if kept[left]:
                    cnt[arrivals[left]] -= 1
                left += 1
            r = arrivals[right]
            if cnt[r] < m:
                cnt[r] += 1
                kept[right] = True
            else:
                discard += 1
        return discard
            
































# from collections import Counter
# class Solution:
#     def minArrivalsToDiscard(self, arrivals: List[int], w: int,m: int) -> int:
#         count = Counter()
#         n = len(arrivals)
#         kept = [False] * n
#         ans = 0
#         for i in range(n):
#             out = i - w
#             if out >= 0 and kept[out]:
#                 count[arrivals[out]] -= 1
#             x = arrivals[i]
#             if count[x] < m:
#                 count[x] += 1
#                 kept[i] = True
#             else:
#                 ans += 1
#         return ans

          
# class Solution:
#     def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
#         # w：窗口长度（天数）  m：每类物品在窗口内最多保留几个
#         # 状态：count[x] = 窗口内被保留的 x 的个数
#         # 答案：每天到货时，放不下就丢弃，ans += 1
#         n = len(arrivals)
#         count = Counter()
#         kept = [False] * n
#         ans = 0
#         for i in range(n):
#             # ① 出：第 i-w 天的物品离开窗口（只有保留的才减）
#             out = i - w
#             if out >= 0 and kept[out]:
#                 count[arrivals[out]] -= 1
#             # ② 进：判断今天的物品放不放得下
#             x = arrivals[i]
#             if count[x] < m:
#                 count[x] += 1
#                 kept[i] = True
#             else:
#                 ans += 1
#         return ans
            
# from collections import Counter
# class Solution:
#     def minArrivalsToDiscard(self, arrivals:list[int], w:int, m:int) -> int:
#         ans = 0
#         count = Counter()
#         kept = [False] * len(arrivals)  
#         for i in range(len(arrivals)):
#             x = arrivals[i]
#             if count[x] < m:
#                 count[x] += 1
#                 kept[i] = True
#             else:
#                 ans += 1
#             left = i - w + 1
#             if left >= 0 and kept[left]:
#                 count[arrivals[left]] -= 1
#         return ans
  





































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