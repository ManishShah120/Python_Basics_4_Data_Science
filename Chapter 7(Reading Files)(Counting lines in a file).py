#counting lines in  file
fhand = open('mbox.txt')
count = 0
for eachline in fhand:
    count = count + 1
print("Total number of lines: ",count)