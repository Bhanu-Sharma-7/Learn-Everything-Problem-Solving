# Python program to find the second largest distinct element in an array.

def second_largest_sorting(arr):
    """Naive approach: sort and find the second distinct largest element."""
    if not arr:
        return -1
    arr = sorted(arr)
    largest = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] != largest:
            return arr[i]
    return -1


def second_largest_two_pass(arr):
    """Two-pass approach: find largest first, then second largest."""
    if not arr:
        return -1
    largest = arr[0]
    for value in arr:
        if value > largest:
            largest = value

    second_largest = -1
    for value in arr:
        if value != largest and value > second_largest:
            second_largest = value

    return second_largest


def second_largest_one_pass(arr):
    """One-pass approach: maintain largest and second largest while scanning."""
    if not arr:
        return -1
    largest = -1
    second_largest = -1
    for value in arr:
        if value > largest:
            second_largest = largest
            largest = value
        elif value != largest and value > second_largest:
            second_largest = value
    return second_largest


if __name__ == '__main__':
    arr = [10, 35, 36, 59, 55, 1]
    print('Array:', arr)
    print('Sorting approach:', second_largest_sorting(arr.copy()))
    print('Two-pass approach:', second_largest_two_pass(arr))
    print('One-pass approach:', second_largest_one_pass(arr))

    arr2 = [10, 10, 10]
    print('\nArray:', arr2)
    print('Sorting approach:', second_largest_sorting(arr2.copy()))
    print('Two-pass approach:', second_largest_two_pass(arr2))
    print('One-pass approach:', second_largest_one_pass(arr2))