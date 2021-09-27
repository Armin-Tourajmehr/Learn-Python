# import bubble sort
from bubble_sort import bubble_sort
# Bucket Sort Algorithm
A = [29, 25, 9, 49, 3, 37, 21, 43]

def bucket_sort():
    n = len(A)
    buckets = [[] for i in range(n)]
    for num in A:
        buckets[num//10] += [num]

    return buckets

bucket = bucket_sort()
Sort_List = []
for i in range(len(A)):
    Sort_List += bubble_sort(bucket[i],len(bucket[i]))

print(Sort_List)