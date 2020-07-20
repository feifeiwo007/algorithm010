class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        dp=[[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if i==j==0: dp[i][j]=grid[i][j]                
                elif i == 0: dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0: dp[i][j] = dp[i - 1][j] + grid[i][j]
                else: dp[i][j]= min(dp[i][j-1],dp[i-1][j])+ grid[i][j]
        return dp[-1][-1]