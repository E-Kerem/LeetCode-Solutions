function frequencySort(nums) {
    // Count the frequency of each number
    const frequencyMap = new Map();
    
    for (const num of nums) {
        frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
    }

    // Create an array from the map entries and sort them
    const freqArray = Array.from(frequencyMap.entries());
    
    // Sort by frequency, and then by the number itself
    freqArray.sort((a, b) => a[1] - b[1] || a[0] - b[0]);

    // Build the sorted result based on the sorted frequency array
    const result = [];
    for (const [num, freq] of freqArray) {
        result.push(...Array(freq).fill(num));
    }
    
    return result;
}