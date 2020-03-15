#The Double Split Patern
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(line)
print(words)
email = words[1]
pieces = email.split('@')
print(pieces)
print(pieces[1])