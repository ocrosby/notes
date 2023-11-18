# Selection Sort

- a simple and efficient sorting algorithm
- works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list

```Python
def selectionSort(arr):
    n = len(arr)
    
    # Traverse through all list elements
    for i in range(n):
        # Find the minimum element in ramining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i] = arr[min_idx]
        arr[min_idx] = arr[i]
        
if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    
    selectionSort(arr)
    
    print("Sorted array")
    for i in range(len(A)):
        print("%d" % A[i], end=" , ")
```