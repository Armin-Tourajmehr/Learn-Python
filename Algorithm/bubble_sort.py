# Bubble Sort Algorithm

Arr = [5, 12, 3, 4, 7, 1, 0, 6, 19, 8, 13, 4, 2, 10, 16]
length = len(Arr)

def bubble_sort(A,n):
    for i in range(n-1):
    # This is simple Controll when There is no
    # need to more navigation
        bubble_Check = False
        for j in range(n - 1 , i , -1):
            if A[j] < A[j - 1]:
                # Swap
                A[j],A[j-1] = A[j-1],A[j]
                bubble_Check = True
        if not bubble_Check:
            break
    return A
# print(bubble_sort(Arr,length))