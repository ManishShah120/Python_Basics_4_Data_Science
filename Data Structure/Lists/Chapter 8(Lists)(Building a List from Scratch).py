stuff = list()  #Constructor form
stuff.append('Book')
stuff.append(99)
print(stuff)
stuff.append('Cookie')
print(stuff)

#Is something in a List?
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)

#Lists are in Order
friends = ['Joseph', 'Glen', 'Sally']
print(friends)
friends.sort()
print(friends)