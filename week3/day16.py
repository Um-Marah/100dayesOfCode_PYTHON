# this program to applay Python tuples part:1 && day:16
thisTuple1 = ()
thisTuple2 = (10,)
thisTuple3 = ("apple","banan","black cherry",2,6,55.5)
print("tuples without items :",thisTuple1)
print("tuples with one itemes only",thisTuple2)
print("tuples with many itemes",thisTuple3)
print("print specific item in tuples by index of item:",thisTuple3[2])
print("print the items of tuples by for loop :\n")
for x in thisTuple3:
    print(x)
del thisTuple1 # delete the tuple from memory so,it is not exesit.
print(thisTuple1)  #get error tuple  deleted
