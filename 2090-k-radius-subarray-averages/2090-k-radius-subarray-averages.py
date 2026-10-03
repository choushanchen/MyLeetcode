class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        window_len = 2 * k +1
        avgs = [-1] * n
        
        if n < window_len:
            return avgs

        window_sum = sum(nums[ :window_len])
        avgs[k] = window_sum // window_len

        for i in range(k + 1, n - k):
            window_sum += nums[i + k] - nums[i - k - 1]
            avgs[i] = window_sum // window_len
        return avgs
