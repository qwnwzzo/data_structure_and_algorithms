## Description (01背包问题)
There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item. What's the maximum value can you put into the backpack?

```
1. A[i], V[i], n, m are all integers.
2. You can not split an item.
3. The sum size of the items you want to put into backpack can not exceed m.
4. Each item can only be picked up once
```

### Examples
```
Example 1:
    Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
    Output: 9
    Explanation: Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9 

Example 2:
    Input: m = 10, A = [2, 3, 8], V = [2, 5, 8]
    Output: 10
    Explanation: Put A[0] and A[2] into backpack, getting the maximum value V[0] + V[2] = 10 
```

### Hint
1. 经典的01背包问题, 资源分配型动态规划
2. 设定 f[i][j] 表示前 i 个物品装入大小为 j 的背包里, 可以获取的最大价值总和. 决策就是第i个物品装不装入背包, 所以状态转移方程就是 f[i][j] = max(f[i - 1][j], f[i - 1][j - A[i]] + V[i])
3. 可以使用滚动数组优化空间至 O(m)

### Solution
```Python
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + V[i - 1])
        
        return dp[n][m]
```