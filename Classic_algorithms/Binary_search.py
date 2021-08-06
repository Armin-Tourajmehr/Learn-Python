# Recursive Binary Search
def Binary_search(data, target, high, low):
    if low > high:
        return False
    else:
        mid = (high + low) // 2
        if data[mid] == target:
            return mid
        elif target > data[mid]:
            return Binary_search(data, target, high, mid + 1)
        else:
            return Binary_search(data, target, mid - 1, low)


def Main():
    array = input('input several number: ').split(' ')
    arr = []
    while True:
        target = input('Enter target: ')
        high = input('Enter high number: ')
        low = input('Enter low number: ')
        if high.isalpha() or low.isalpha() or target.isalpha():
            print(f'Please enter digit number')
        else:
            for i in array:
                arr.append(int(i))
            target = int(target)
            high = int(high)
            low = int(low)
            print(Binary_search(arr, target, high, low))
            question = input('Do you want to continue (Y/N): ').lower()
            if question[0] == 'n':
                break


if __name__ == '__main__':
    Main()
