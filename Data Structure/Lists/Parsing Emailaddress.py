fhand = open('mbox-short.txt')
for eachline in fhand:
    eachline = eachline.rstrip()
    words = eachline.split()
    #guardian in a compound statement
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])