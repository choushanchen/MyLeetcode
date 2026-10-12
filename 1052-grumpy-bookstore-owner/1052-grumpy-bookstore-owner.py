class Solution:
    def maxSatisfied(self, customers: list[int], grumpy:list[int], minutes:int) -> int:
        ans = 0 
        count = 0
        n = len(customers)
        for i in range(n):
            if grumpy[i] == 0:
                 count += customers[i]
        win_arg = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        count += win_arg
        ans = count 
        for i in range(minutes, n):
            if grumpy[i] == 1:
                count += customers[i]
            if grumpy[i - minutes] == 1:
                count -= customers[i -minutes]
            ans = max(count, ans)
        return ans


# class Solution:
#     def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
#         count = 0
#         for i in range(len(grumpy)):
#             if grumpy[i] == 0:
#                 count += customers[i]
        
#         win_stf = sum(customers[i] for i in range(minutes) if grumpy[i] != 0)
#         max_stf = win_stf + count
#         for i in range(1, len(customers) - minutes + 1):
#             if grumpy[i + minutes -1] == 1:
#                 win_stf += customers[i + minutes - 1]
#             if grumpy[i - 1] == 1:
#                 win_stf -= customers[i - 1]
#             if win_stf + count > max_stf:
#                 max_stf = win_stf + count
#         return max_stf



        