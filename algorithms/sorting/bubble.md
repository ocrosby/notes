# Bubble Sort

- the simplest sorting algorithm
- works by repeatedly swapping the adjacent elements if they are in the wrong order

- traverse from left and compare adjacent elements and the higher one is placed on the right side
- in this way, the largest element is moved to the rightmost end at first
- the process is then continued to find the second largest and place it and so on until the data is sorted

```Python
def bubbleSort(arr):
    n = len(arr)
    
    # traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if (swapped == False):
            break
            
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(arr)
    
    print("Sorted array is:")    
    for i in range(len(arr)):
        print("%d" %arr[i])
```
 
In this case we have n=7 elements in the array.

The following table illustrates the process:

| i | j | j+1 | n-i-1 | arr[j] | arr[j+1] | arr[j] > arr[j+1] | swapped | arr |
|---|---|-----|-------|--------|----------|--------------------|---------|-----|
| 0 | 0 | 1   | 6     | 64     | 34       | True               | True    | [34, 64, 25, 12, 22, 11, 90] |
| 0 | 1 | 2   | 6     | 64     | 25       | True               | True    | [34, 25, 64, 12, 22, 11, 90] |
| 0 | 2 | 3   | 6     | 64     | 12       | True               | True    | [34, 25, 12, 64, 22, 11, 90] |
| 0 | 3 | 4   | 6     | 64     | 22       | True               | True    | [34, 25, 12, 22, 64, 11, 90] |
| 0 | 4 | 5   | 6     | 64     | 11       | True               | True    | [34, 25, 12, 22, 11, 64, 90] |
| 0 | 5 | 6   | 6     | 64     | 90       | False              | True    | [34, 25, 12, 22, 11, 64, 90] |
| 1 | 0 | 1   | 5     | 34     | 25       | True               | True    | [25, 34, 12, 22, 11, 64, 90] |
| 1 | 1 | 2   | 5     | 34     | 12       | True               | True    | [25, 12, 34, 22, 11, 64, 90] |
| 1 | 2 | 3   | 5     | 34     | 22       | True               | True    | [25, 12, 22, 34, 11, 64, 90] |
| 1 | 3 | 4   | 5     | 34     | 11       | True               | True    | [25, 12, 22, 11, 34, 64, 90] |
| 1 | 4 | 5   | 5     | 34     | 64       | False              | True    | [25, 12, 22, 11, 34, 64, 90] |
| 2 | 0 | 1   | 4     | 25     | 12       | True               | True    | [12, 25, 22, 11, 34, 64, 90] |
| 2 | 1 | 2   | 4     | 25     | 22       | True               | True    | [12, 22, 25, 11, 34, 64, 90] |
| 2 | 2 | 3   | 4     | 25     | 11       | True               | True    | [12, 22, 11, 25, 34, 64, 90] |
| 2 | 3 | 4   | 4     | 25     | 34       | False              | True    | [12, 22, 11, 25, 34, 64, 90] |
| 3 | 0 | 1   | 3     | 12     | 22       | False              | True    | [12, 22, 11, 25, 34, 64, 90] |
| 3 | 1 | 2   | 3     | 22     | 11       | True               | True    | [12, 11, 22, 25, 34, 64, 90] |
| 3 | 2 | 3   | 3     | 22     | 25       | False              | True    | [12, 11, 22, 25, 34, 64, 90] |
| 4 | 0 | 1   | 2     | 12     | 11       | True               | True    | [11, 12, 22, 25, 34, 64, 90] |
| 4 | 1 | 2   | 2     | 12     | 22       | False              | True    | [11, 12, 22, 25, 34, 64, 90] |
| 5 | 0 | 1   | 1     | 11     | 12       | False              | True    | [11, 12, 22, 25, 34, 64, 90] |
| 6 | 0 | 1   | 0     | 11     | 12       | False              | True    | [11, 12, 22, 25, 34, 64, 90] |


