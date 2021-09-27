# Selecion Sort Algorithm
myList = [12, 3, 15, -4, 7, 6, -1, 0, 11, 6]

def selection_sort(List):
    n = len(List)
    for i in range(n - 1):
        index = i
        for j in range(n - 1 , 1 , -1):
            if List[index] > List[j]:
                index = j
        List[i],List[index] = List[index],List[i]
    return List

Sort = selection_sort(myList)
print(Sort)