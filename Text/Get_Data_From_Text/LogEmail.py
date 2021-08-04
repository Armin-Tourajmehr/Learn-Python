# computing log email and in the end it computes who sends the most emails
fh = input('Enter File : ')
try:
    x = fh.split()
    log = open(fh)

    dictionary = dict()
    largest = -1
    word = None
    for line in log:
        line = line.split()
        if len(line) == 0 or line[0] != 'From': continue
        li = line[1]
        dictionary[li] = dictionary.get(li, 0) + 1
        for w, l in dictionary.items():
            if l > largest:
                largest = l
                word = w

        # This is another way to solve
        """
        for ch in d:
            if largest is None or d[ch] > largest :
                largest = d[ch]
        x = list(d.keys())
        for i in x:
            if d[i] == largest:
                y = i   
        """

        print(word, largest)
        print('Done!')

except:
    print('Your File',fh,'cannot be open')
    quit()



