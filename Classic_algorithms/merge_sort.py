# Merge Sort
# First find the middle point to divide the array into the havles:
# middle = l + (r-1)/2
def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        # right half
        right = arr[middle:]
        # left half
        left = arr[:middle]
        # Call the merge
        mergeSort(right)
        mergeSort(left)

        i = j = k = 0

        # Copy data to temp arrays right[] and  left[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i] ,end=' ')
    print()

if __name__ == '__main__':
    arr = [12,11,13,8,3,5,6,19,7]
    print('Given array is',end='\n')
    printList(arr)
    mergeSort(arr)
    print('Sorted array is',end='\n')
    printList(arr)
