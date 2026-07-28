class Solution:
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]   # Copy last row

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
        
        