## Description
Given an integer array nums[] which contains n unique positive numbers, num[i] indicate the size of ith item. An integer target denotes the size of backpack. Find the number of ways to fill the backpack.

### Hint
f[i][j]表示只考虑前i件物品，取到物品重量和为j的方法数量，这题和完全背包做法类似

### Solution
```Python
class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: The maximum value
    """
    def backPackIV(self, nums, target):
        n = len(nums)
        m = target
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j:
                    dp[i][j] += dp[i][j - nums[i - 1]]
        
        return dp[n][m]
```