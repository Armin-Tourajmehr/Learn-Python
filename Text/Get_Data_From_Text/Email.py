# File Handle
fh = input('Enter your file : ')
try:
    mbox = open(fh)

    dictionary = dict()
    for line in mbox:
        line = line.split()
        if len(line) == 0 or line[0] != 'From': continue
        li = line[3]
        dictionary[li] = dictionary.get(li, 0) + 1
    print(dictionary)

except:
    print('file', fh, 'cannot be open!!!, please try again')

