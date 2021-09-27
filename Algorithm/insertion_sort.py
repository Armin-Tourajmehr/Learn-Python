# This is Insertion Sort Algorithm
# Complexity Time is O(n^2)

A = [9,7,2,3,6,2,1,5,8,20,10]

# Array's Length
n = len(A)
for i in range(1, n):
    # placeholder for index and number which of index
    # point to it
    insertion = i
    temp = A[i]

    # Main code
    while insertion > 0 and temp < A[insertion - 1] :
        # Swap
        A[insertion] = A[insertion - 1]
        insertion -= 1
    A[insertion] = temp

print(A)

