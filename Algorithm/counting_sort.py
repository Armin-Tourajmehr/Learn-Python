# This is a "COUNTING SORT" algorithm

# time complexity for this algorithm is :
# T(n) = O(2n)
# n perfomance is for first loop and 
# alternavtive n perfomance is for second loop
# when add both them (n + n = 2n)
# BE CAREFUL ---> the input number should be
# discrete and shouldn't be too large


array = [5,5,2,4,3,2,5,6,2,1,1,3,4,8,9,6,8]

# we should know what is the largest number in array
Max = max(array)
# This is just a Count List to help us count how many numbers that
# have duplicated in array List   
Count = [0] * (Max + 1)

# packing Count List 
for i in array:
    Count[i] += 1

# print(Count)
# PART 2 (Sorting)
sort_list = []
for x in range(Max + 1):
    sort_list += [x] * Count[x]

print(sort_list)