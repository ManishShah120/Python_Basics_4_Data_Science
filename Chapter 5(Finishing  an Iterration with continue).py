while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'Done':
        break
    print(line)
print('Done!!')