#File Handle as a sequence
xfile = open('mbox.txt','r')  #xfile is the handle
for eachline in xfile:
    print(eachline)