def Len(List):
    i = 0
    j = ''
    for word in List:
        if i < len(word):
            i = len(word)
            j = word
    return j


def main():
    List = list()
    number = int(input('how many do you like yo input words: '))
    for num in range(0, number):
        words = input('Enter a words: ')
        List.append(words)
    print(Len(List))


main()
