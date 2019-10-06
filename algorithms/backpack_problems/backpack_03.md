## Description (完全背包问题)
Given n kinds of items, and each kind of item has an infinite number available. The i-th item has size A[i] and value V[i]. Also given a backpack with size m. What is the maximum value you can put into the backpack?

### Hint
1. 类似于最基本的01背包, 我们设定 f[i][j] 表示前 i 种物品装到容量为 j 的背包里, 能获取的最大价值为多少.
2. 比较简单的转移是直接枚举第i种物品取用多少个: f[i][j] = max{f[i - 1][j - x * A[i]] + x * V[i]}
3. 但是这样速度较慢, 可以优化成 f[i][j] 直接由 f[i][j - A[i]] 转移, 并且从小到大枚举 j, 这样做的含义就是在已经拿过第 i 个物品的之后还可以再拿它. 也就是说: 计算 f[i][j] 时, 初始设置为 f[i - 1][j], 然后 f[i][j] = max(f[i][j], f[i][j - A[i]] + V[i])
4. 另外, 可以使用滚动数组优化, 使用滚动数组之后也不必要手动设置 f[i][j] = f[i - 1][j], 与01背包使用的滚动数组相反, 这里恰好需要正着枚举容量 j, 因而有 f[j] = max(f[j], f[j - A[i]] + V[i])

### Solution
```Python
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackIII(self, m, A, V):
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if A[i - 1] <= j:
                    dp[i][j] = max(dp[i][j], dp[i][j - A[i - 1]] + V[i - 1])
        
        return dp[n][m]
```