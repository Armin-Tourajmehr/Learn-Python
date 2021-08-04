# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    # Traverse Through all every elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed
        for j in range(n - i - 1):
            # Traverse the array from 0 to n-i-1
            # swap if the element found is greater
            # then the next element
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]




if __name__ == '__main__':
    arr = [1, 32, 45, 6, 2, 47, 13, 53, 78, 133, 54, 23, 44]
    bubbleSort(arr)
    for i in range(len(arr)):
        print('%d'%arr[i],end=' ')
