fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):#If the line doesnt start with From then continue
        continue
    print(line)