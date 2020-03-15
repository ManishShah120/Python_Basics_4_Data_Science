filename = input('Enter te file name: ')
try:
    fhand = open(filename)
except:
    print('Oops File cannot be Opened:', filename)
    quit()


count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', filename)