1. **Problem Understanding**: 
   We need to identify users who have used their key-card 3 or more times within any one-hour window. 

2. **Input Handling**:
   - The function takes two arrays: `keyName` (the names of users) and `keyTime` (the corresponding times when the key-cards were swiped).
   - Each time in `keyTime` is in the form "HH:MM".

3. **Time Conversion**:
   - For convenience, convert each time from "HH:MM" to minutes since midnight. This gives us a straightforward way to compare time differences.

4. **Storing Times**:
   - A hashmap (`timeMap`) is created to associate key-card holders (names) with their swipe times in minutes. 

5. **Sorting and Checking**:
   - For each key-name, we retrieve their associated list of swipe times and sort it.
   - We then iterate through the sorted list of times, checking if the difference between the time two indices apart is 60 minutes or less. If so, we can alert the user and stop checking further for that name.

6. **Result Compilation**:
   - The names found are collected into `alertNames`, which then gets sorted alphabetically before being returned.