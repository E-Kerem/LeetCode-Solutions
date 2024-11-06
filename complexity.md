1. **Time Complexity**:
   - The time complexity of this solution is **O(n)**, where `n` is the length of the input string `command`. This is because we make a single pass through the string, processing each character in constant time.

2. **Space Complexity**:
   - The space complexity is **O(1)**, if we disregard the space used by the `StringBuilder`, as we are using a fixed amount of extra space (the `StringBuilder` is our output and its size grows proportional to the length of the output rather than the input).
   - Technically, considering the output space in `StringBuilder`, it can also be considered **O(n)** for the output size, but this is purely for the result returned.

Thus, the solution is efficient and adheres to the problem constraints well.