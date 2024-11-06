class Solution:
    def countPaths(self, grid: List[List[int]], k: int) -> int:
        from collections import defaultdict
        
        # Define the dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Create a 3D dp table to store the count of paths
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Initialize the starting point
        dp[0][0][grid[0][0] % k] = 1
        
        # Iterate through the entire grid
        for i in range(m):
            for j in range(n):
                for mod in range(k):
                    if dp[i][j][mod] > 0:
                        # Move downwards
                        if i + 1 < m:
                            new_mod = (mod + grid[i + 1][j]) % k
                            dp[i + 1][j][new_mod] += dp[i][j][mod]
                        # Move to the right
                        if j + 1 < n:
                            new_mod = (mod + grid[i][j + 1]) % k
                            dp[i][j + 1][new_mod] += dp[i][j][mod]
        
        # Sum all paths that are divisible by k
        return sum(dp[m - 1][n - 1]) % (10**9 + 7)