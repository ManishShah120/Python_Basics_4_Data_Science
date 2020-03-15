#To check how many times we itterate a loop
count =0
total =0
for number in [9,41,12,3,74,15]:
    count = count+1
    total = total + number
    print(count,number)
print("The loop runs",count,"times")
print("The sum of all the numbers is",total)
print("The average of all the number is",(total)/count)