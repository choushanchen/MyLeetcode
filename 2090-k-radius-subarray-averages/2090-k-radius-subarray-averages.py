class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        win_len = 2*k + 1 

        if n < win_len:
            return ans

        win_sum = sum(nums[ :win_len]) 
        ans[k] = win_sum // win_len

        for i in range (k + 1, n - k):
            win_sum += nums[i + k] - nums[i - k - 1]
            ans[i]= win_sum // win_len
        return ans      



# 第一次做的答案
# class Solution:
#     def getAverages(self, nums: list[int], k: int) -> list[int]:
#         n = len(nums)
#         window_len = 2 * k +1
#         avgs = [-1] * n
        
#         if n < window_len:
#             return avgs

#         window_sum = sum(nums[ :window_len])
#         avgs[k] = window_sum // window_len

#         for i in range(k + 1, n - k):
#             window_sum += nums[i + k] - nums[i - k - 1]
#             avgs[i] = window_sum // window_len
#         return avgs
