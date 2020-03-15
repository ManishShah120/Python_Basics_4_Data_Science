#Built-in Functions and Lists
'''
nums  = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
'''


# A program to compute the average of any entered numbers
#Doesnt uses more memory
total = 0
count = 0
while True:
    inp = input('Enter a number:')
    if(inp == 'done'):
        break
    value = int(inp)
    count = count + 1
    total = total + value
average = total/count
print('Avergage: ',average)
print(type(inp))
print(inpu)  #Traceback

#A program to compute the average of any entered number
#Uses more memory
numlist = []  #or numlist = list()
while True:
    inpu = input('Enter a number: ')
    if inpu == 'done':
        break
    value = int(inpu)
    numlist.append(value)
averaga = sum(numlist)/len(numlist)
print(averaga)
print(type(numlist))
print(numlist)
