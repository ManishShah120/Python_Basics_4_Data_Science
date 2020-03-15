#Time Stamp 4:29:01
'''
List:- A linear collection of values that stay in order
Dictionary:- A "bag" of values, each with its own label
'''
'''
-->Lists index their entries based on the 
   position in the list.
   
-->Dictionaries are like bags - No Order

-->So we index the things we put in the dictionary with a 
   "Lookup tag"
'''
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print("The type of Purse is",type(purse))
purse['candy'] = purse['candy'] + 2
print(purse)