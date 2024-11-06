1. **Time Complexity**:
   - Counting frequencies takes O(n), where n is the length of the input array `nums`.
   - Sorting the frequency array takes O(k log k), where k is the number of unique elements in `nums`.
   - Overall, the time complexity can be expressed as O(n + k log k).
   - In the worst case, every number is unique (k = n), so the time complexity simplifies to O(n log n).

2. **Space Complexity**:
   - We use additional space for the `Map` and the result array. The space taken by the frequency map is O(k) and the result array is O(n).
   - Therefore, the overall space complexity is O(n).

This gives us the complete solution along with an explanation, visualization steps, and a complexity analysis for the problem "Sort Array by Increasing Frequency".