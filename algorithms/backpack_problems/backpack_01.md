## Description
Given n items with size A, an integer m denotes the size of a backpack. How full you can fill this backpack? (You can not divide any item into small pieces.)

### Examples
```
Example 1:
    Input:  [3,4,8,5], backpack size=10
    Output:  9

Example 2:
    Input:  [2,3,5,7], backpack size=12
    Output:  12
```

### Solution 1 : O(n x m) time and O(n x m) memory
```Python
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        num_items = len(A)
        
        # dp[i][j]表示前i个物品选一些物品放入容量为j的背包中能否放满。
        dp = [[False] * (m + 1) for i in range(num_items + 1)]
        for i in range(num_items + 1):
            dp[i][0] = True
        
        for i in range(1, num_items + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= A[i - 1] and dp[i - 1][j - A[i - 1]] is True:
                    dp[i][j] = True
        
        for i in range(m, 0, -1):
            if dp[num_items][i] is True:
                return i
        
        return 0
```

### Solution 2 : O(n x m) time and O(m) memory
```Python
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        num_items = len(A)
        
        dp = [0 for _ in range(m + 1)]
        for i in range(num_items):
            j = m
            while j >= A[i]:
                dp[j] = max(dp[j], dp[j - A[i]] + A[i])
                j -= 1
        
        return dp[m]
```