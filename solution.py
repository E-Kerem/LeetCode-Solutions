def maxSubsetSize(nums):
    # Sort the input list
    nums.sort()
    
    max_size = 0
    current_sum = 0
    
    for num in nums:
        # Check if adding the current number doesn't exceed the limit of 1
        if current_sum + num <= 1:
            current_sum += num
            max_size += 1
            
    return max_size