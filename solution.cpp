#include <vector>
#include <algorithm>

class Solution {
public:
    int minRemoval(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;

        // dp[i] will store the length of longest increasing subsequence ending with the ith element
        std::vector<int> dp(n, 1);

        // Fill dp array to find lengths of increasing subsequences
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j]) {
                    dp[i] = std::max(dp[i], dp[j] + 1);
                }
            }
        }

        // The length of the longest increasing subsequence
        int lisLength = *std::max_element(dp.begin(), dp.end());

        // We need to remove (n - lisLength) subsequences to achieve the final array
        return lisLength > 0 ? n - lisLength : n;
    }
};