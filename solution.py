def countDistinctIntegers(nums):
    def reverse_number(n):
        return int(str(n)[::-1])
    
    distinct_numbers = set(nums)
    
    for num in nums:
        reversed_num = reverse_number(num)
        distinct_numbers.add(reversed_num)
    
    return len(distinct_numbers)

# Example usage:
nums = [123, 456, 789]
print(countDistinctIntegers(nums))  # Output: 6