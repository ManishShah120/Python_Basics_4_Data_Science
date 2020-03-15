#A lot of spaces
line = 'A lot               of spaces'
etc = line.split()  #splits job is  to split things based on spaces
print(line)
print(etc)
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')  #splits based on semicolon
print(thing)
