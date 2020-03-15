#WAP to find the largest Number
numbers = [23,-1,23,9,0,81,32,2,91,23,2,1,77,23,12.01,12.081]
maximum = max(numbers)
minimum = min(numbers)
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
        print("Till Now largest is",largest)
print(largest)
print("The largest number among the numbers is",maximum)
print("The largest number among the numbers is",minimum)