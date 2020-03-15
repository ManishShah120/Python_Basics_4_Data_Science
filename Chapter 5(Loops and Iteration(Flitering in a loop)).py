#To find the numbers which are greater than 20
#count =0
#for number in [9,41,12,3,74,15]:
#    count = count+1
#    #print(count,number)
#    if number > 20:
#        print(number,"is greater than 20")
#2:45 time of the video
#How to store the entered number in an array?
numbers = {}
size = int(input('Enter the size of the array:-'))
print('Enter the elements of the array:')
for i in range(0,size):
    numbers[i] = int(input("> "))
print("The entered numbers are:-")
for i in range(0,size):
    print("Number{",i,"}",numbers[i])