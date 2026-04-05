Day 1 - Second Largest Element in an Array

Task: Given an array of positive integers `arr[]` of size `n`, find the second largest distinct element in the array.
If the second largest element does not exist, return `-1`.

Examples:

- input: `arr[] = [10, 35, 36, 59, 55, 1]`
  output: `55`
  explanation: the largest value is `59`, the second largest distinct value is `55`.

- input: `arr[] = [10, 10, 10]`
  output: `-1`
  explanation: all values are the same, so there is no second largest distinct value.

Table of contents:

- naive approach using sorting
- better approach using two-pass search
- best approach using one-pass search

Naive approach using sorting:

1. Sort the array.
2. Start from the largest value at the end.
3. Move left until you find a value that is different from the maximum.
4. That value is the second largest distinct element.

This approach is simple, but sorting takes `O(n log n)` time.

Better approach using two-pass search:

1. First pass: find the maximum value in the array.
2. Second pass: find the largest value that is not equal to the maximum.

This uses `O(n)` time and `O(1)` extra space.

Best approach using one-pass search:

1. Keep two variables: `largest` and `second_largest`.
2. For each number, update `largest` and `second_largest` in one scan.

This is the fastest approach because it uses only one loop and `O(1)` extra space.

