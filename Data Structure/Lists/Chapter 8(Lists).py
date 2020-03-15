#Time Stamp 3:48:56
#Lists
'''
Collections
A list is a kind of a collection
friends = ['Joseph', 'Glenn', 'Sally']
'''
print([1,23,76])  #List
'''
>Lists are surrounded by Square brackets
 and the elements in the lists are separated by commas
>A list element can be any Python object-even another list
'''
print(['Red', 'Yellow', 'Blue'])
print(type(['Red', 'Yellow', 'Blue']))
print([1, [5, 6], 7])
print(type([1, [5, 6], 7]))
print([])
print(type([]))

#Using list in for loops
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Fineshed')