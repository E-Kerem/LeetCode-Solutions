The solution can be outlined in the following steps:

1. **Counting Frequencies**: 
   - We use a `Map` called `frequencyMap` to count the occurrences of each number in the input array `nums`.
   - We iterate over each number in `nums`, and for each number, we increment its frequency in the `frequencyMap`.

2. **Preparing for Sorting**:
   - We convert the `Map` into an array of entries using `Array.from(frequencyMap.entries())`. Each entry consists of a number and its corresponding frequency.

3. **Sorting Entries**:
   - We sort the frequency array using the `sort` method. The sorting is done based on two criteria:
     - First by frequency in ascending order (`a[1] - b[1]`).
     - If the frequencies are the same, we sort the numbers themselves in ascending order (`a[0] - b[0]`).

4. **Building the Result Array**:
   - We then build our final sorted result array. For each entry in the sorted frequency array, we fill the result array with the number repeated according to its frequency. We use `Array(freq).fill(num)` to create an array of `num` repeated `freq` times, and then spread this into the result.

5. **Return the Result**: Finally, we return the `result` array which now contains the numbers sorted by their frequency.