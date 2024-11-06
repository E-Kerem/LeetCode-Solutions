### Step-by-Step Solution

1. **Initialization**:
   - We import `defaultdict` from the `collections` module.
   - We determine the dimensions `m` and `n` of the grid.
   - A 3D list `dp` is created. `dp[i][j][mod]` will hold the number of paths leading to cell `(i,j)` with a sum that modulo `k` equals `mod`.

2. **Base Case**:
   - The starting point is initialized. The number of paths to the first cell `(0,0)` with a sum that modulo `k` equals `grid[0][0] % k` is set to `1`.

3. **Dynamic Programming Iteration**:
   - We iterate through each cell in the grid using two nested loops (for rows `i` and columns `j`).
   - For each cell `(i,j)`, we check every possible modulo value (`mod`) from `0` to `k-1`.
   - If paths exist to this cell with a certain sum modulo `k`, we attempt to extend these paths:
     - **Downward Move**: If not at the last row, move to cell `(i+1, j)` and update the new modulo value.
     - **Rightward Move**: If not at the last column, move to cell `(i, j+1)` and update its modulo value likewise.

4. **Final Count**:
   - After finishing all iterations, we sum up all the paths that reach the bottom-right corner `(m-1, n-1)` whose sum's modulo `k` equals `0`.
   - We return this value modulo `10^9 + 7` to handle large numbers.