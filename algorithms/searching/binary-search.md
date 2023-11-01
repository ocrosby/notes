# Binary Search

## Definition

Binary search is a searching algorithm that searches a sorted list for a target value by repeatedly dividing the search interval in half. The algorithm begins by comparing the target value to the value of the middle element of the sorted list. If the target value is equal to the middle element's value, then the position is returned and the search is finished. If the target value is less than the middle element's value, then the search continues on the lower half of the list. If the target value is greater than the middle element's value, then the search continues on the upper half of the list. This process continues until the target value is found or the interval is empty.

## Example

Given a sorted list of numbers and a target value, return the index of the target value in the list. If the target value is not found in the list, return -1.

```python
def binary_search(arr, target):
    """
    Search a sorted list for a target value using binary search.
    This algorithm has a time complexity of O(log n).
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
    
if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    target = 11
    
    result = binary_search(my_list, target)
    
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the list.")
```

## References

- [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)
- [Geeks for Geeks](https://www.geeksforgeeks.org/binary-search/)
- [Tutorialspoint](https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm)
- [Programiz](https://www.programiz.com/dsa/binary-search)
