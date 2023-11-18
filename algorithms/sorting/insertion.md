# Insertion Sort

- similar to the way you sort playing cards in your hands
- array is virtually split into a sorted and unsorted part
- values from the unsorted part are picked and placed at the correct position in the sorted part

To sort an array of size N in ascending order iterate over the array and compare the 
current element (key) to its predecessor, if the key element is smaller than its 
predecessor, compare it to the elements before.  Move the greater elements one position
up to make space for the swapped element.

```Python
# Python program for implementation of Insertion Sort
 
# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    
    insertionSort(arr)
    
    for i in range(len(arr)):
        print ("% d" % arr[i])
```