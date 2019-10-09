# this program to applay about Python Sets Methods day:21
girlSet = {"Sarah","Marah","Lames","Amal","Rawan","zahra","Wesam"}
boySet = {"Ali","mohammed","Yosif","waleed","Hammam","Bassam","Wesam"}
#len()Method
print("lenth of girlSet =",len(girlSet))
print("lenth of boySet =",len(boySet))
#copy()Method
y = girlSet.copy()
print("the copy from girlSet: y =",y)
#difference()Method
print("items that are in boySet but not in girlSet:(boySet-girlSet)= ",boySet.difference(girlSet))
print("items that are in girlSet but not in boySet:(girlSet-boySet)= ",girlSet.difference(boySet))
#difference_update()method
print("removes the items that exist in both sets: ",girlSet.difference_update(boySet))
#add()method
girlSet.add("Eman")
print("add item to the girlSet :",girlSet)
#intersection() method
z=girlSet.intersection(boySet)
print("returns a set that contains the similarity between two or more sets:", z)
#intersection_update()
boySet.intersection_update(girlSet) 
print("method removes the items that is not present in both sets:",boySet )
#isdisjoint() method
x = boySet.isdisjoint(girlSet) 
print("returns True if none of the items are present in both sets, otherwise it returns False :-",x)
#The issubset() method
a = boySet.issubset(girlSet) 
print("returns True if all items in the set exists in the specified set, otherwise it retuns False :-",a)
#The issuperset() method
b = girlSet.issuperset(boySet) 
print("returns True if all items in the specified set exists in the original set, otherwise it retuns False :-",b)
#The symmetric_difference() method
c= girlSet.symmetric_difference(boySet) 
print("returns a set that contains all items from both set, but not the items that are present in both sets :-",c)
#The symmetric_difference_update() method
girlSet.symmetric_difference_update(boySet) 
print("updates the original set by removing items that are present in both sets, and inserting the other items :- ",girlSet)
# union()method
d = boySet.union(girlSet) 
print("returns a set that contains all items from the original set, and all items from the specified sets :- ",d)
#The update() method
boySet.update(girlSet) 
print("updates the current set, by adding items from another set :-",boySet)
#remove()
girlSet.remove("Amal")
print("Removes the specified element from the set:- ",girlSet)
#pop()	
print("Removes an element from the set:-",girlSet.pop())
#clear()
girlSet.clear()
print("Removes all the elements from the set",girlSet)