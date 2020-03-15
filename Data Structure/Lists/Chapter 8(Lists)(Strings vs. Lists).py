#Best Friends: Strings and Lists

abc = 'With three words'  #abc is a list of words
print(abc)
print(type(abc))
print(abc[0])
#abc[0] = 'W'  #Not possible because string doesnt support Mutation

stuff = abc.split()  #Stuff is list of strings i.e., split return a list of individual words
print(stuff)
print(type(stuff))
print(stuff[0])
stuff[0] = 'X'
print(stuff[0])
print(stuff)

'''
SPLIT breaks a string into parts and produces a list 
and produces a list of strings. We think of these as words.
we can ACESS a particular word or LOOP through all the words. 
'''


#Time Stamp: 4:11:29

