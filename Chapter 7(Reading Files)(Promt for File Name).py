filename = input('Enter te file name: ')
fhand = open(filename)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', filename)