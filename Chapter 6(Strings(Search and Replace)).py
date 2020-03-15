greet = 'Hello BOB'
snr = greet.replace('BOB','Manish')
print(snr)
snr1 = greet.replace('l','X')
print(snr1)

#Stripping Whitespace
groot = '   Hello Bob   '
print(groot)
check1 = groot.lstrip()#sTRIPS THE SPACES ON THE LEFT
print(check1)
check2 = groot.rstrip()#Strips the spaces on the right
print(check2)
check3 = groot.strip()#Strips the spaces from both the sides
print(check3)


#Prefixes
line = 'Please hae a nice day'
line1 = line.startswith('Please')
print(line1)