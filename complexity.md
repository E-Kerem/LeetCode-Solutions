### Time Complexity:
- The outer loop runs `n` times.
- The inner loop will, in the worst case, run up to `√n` times for each `i`, which means the overall time complexity is:
  \[
  O(n \sqrt{n})
  \]
  
### Space Complexity:
- The space complexity is \(O(n)\) due to the `dp` array used to store the intermediate results.

Thus, the algorithm is efficient and leverages dynamic programming to arrive at the solution optimally.