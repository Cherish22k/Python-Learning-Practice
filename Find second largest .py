#CODE

def second_largest(arr):
    if len(arr) < 2:
        return None

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

# Example
numbers = [10, 20, 4, 45, 99]
print("Second largest:", second_largest(numbers))
