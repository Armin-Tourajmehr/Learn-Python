# search in data & computing number of date
import string

fh = input('Enter file : ')
try:
    romeo = open(fh)
    rd = dict()
    for line in romeo:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        word = line.split()
        for ch in word:
            if ch not in rd:
                rd[ch] = 1
            else:
                rd[ch] = rd[ch] + 1
    print(rd)
except:
    print('your file',fh,'cannot be open')
    quit()




