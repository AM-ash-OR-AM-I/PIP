# User function Template for python3
import math


class Solution:
    def findMinOpeartion(self, matrix, n):
        max_rows_sum = 0
        rows_sum_arr = [0] * n
        cols_sum_arr = [0] * n
        for i in range(n):
            cols_sum = rows_sum = 0
            for j in range(n):
                cols_sum += matrix[j][i]
                rows_sum += matrix[i][j]
            cur_max = max(cols_sum, rows_sum)
            max_rows_sum = max(max_rows_sum, cur_max)
            rows_sum_arr[i] = rows_sum
            cols_sum_arr[i] = cols_sum
        min_ops = 0
        for i in range(n):
            min_ops += (max_rows_sum - cols_sum[i]) + (max_rows_sum - rows_sum[i])
        return min_ops // 2


for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
