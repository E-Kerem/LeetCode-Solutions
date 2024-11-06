public class PerfectSquares {
    public int numSquares(int n) {
        // Create a DP array with a size of n + 1
        int[] dp = new int[n + 1];
        // Initialize the DP array
        for (int i = 1; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE; // max starting value
        }
        
        // Populate the DP array
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        
        // Return the result for n
        return dp[n];
    }

    public static void main(String[] args) {
        PerfectSquares ps = new PerfectSquares();
        int n = 12; // Example input
        System.out.println(ps.numSquares(n)); // Output should be 3 (4 + 4 + 4)
    }
}