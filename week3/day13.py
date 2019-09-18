# this to applay List in paython part:1 && day 13
s =[]    #define list with out elements
print(s)
#access the items of list by index of the item
thisList= ["apple","lemon","banana",22,30,40,4.85,44.5,500,50]
print (thisList[3])
# loop through the list items by using a for loop
myList=[100,200,300]
for x in myList:
   print(x)
# to change the value of specific item in the list
thisList[2] = "black cherry"  
print(thisList)
# to delete specfic item in list
del thisList[2]
print(thisList)
# to delete the list from memory
del thisList
print(thisList)#her become error becouse i delet the list
