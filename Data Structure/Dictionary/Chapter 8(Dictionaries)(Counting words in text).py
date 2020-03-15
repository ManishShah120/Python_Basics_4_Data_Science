#Counting Words in Text
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Conting...')
#Algorithm to count Words
counts = dict()
for word in words:
    counts[word] = counts.get(word,0)+1
print('Counts',counts)
#TimeStamps:- 4:48:34