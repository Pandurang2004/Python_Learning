def find_second_largest(nums):
    """
    Find the second largest number in the list without sorting.
    """
    if len(nums) < 2:
        raise ValueError("List must contain at least two elements.")

    first = second = float('-inf')  # initialize to negative infinity

    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    if second == float('-inf'):
        raise ValueError("No second largest element found (all elements may be equal).")

    return second


# Example usage:
print(find_second_largest([10, 20, 4, 45, 99]))  # Output: 45
print(find_second_largest([5, 5, 5]))            # Raises ValueError
