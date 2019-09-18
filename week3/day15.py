# this to applay List in paython part:3 paython List methods && day 15
thisList= ["apple","lemon","banana",22,30,40,4.85,44.5,500,50]
#to determine how many items in the list use 'len() method'.
print(len(thisList))
# to add items in the list use 'append() method'.
thisList.append("marah")
print(thisList)
#to add an item at the specified index, use the insert() method.
thisList.insert(3, "orange")
print(thisList)
# to remove specific item from list use remove() method.
thisList.remove("marah")
print(thisList)
# to remove last item from list use pop() method.
thisList.pop()
print(thisList)
#to remove specific index from list use pop() method.
thisList.pop(1)
print(thisList)
# to copy the list to another list use the copy()method or list() method .
myList = thisList.copy()
anotherList = list(thisList)
print(myList)
print(anotherList)
# list () constructor
thisList = list(("chrrey","banana","orange"))
print(thisList)
#sort the list by sort()method.
thisList.sort()
print(thisList)
# reverse the list by reverse()method.
thisList.reverse()
print(thisList)
#extend the list by exetend()method
thisList.extend(myList)
print(thisList)
# return the index of specific element
print(thisList.index("orange"))
