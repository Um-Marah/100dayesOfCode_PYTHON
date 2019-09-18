# this program to applay Python tuples part:2 && day:17
namesOfGirls = ("marah","malath","melaf","mela")
print("the number of item in the list:\n",len(namesOfGirls))
print("count how  many specific item appear in the list example item 'marah':\n")
print(namesOfGirls.count("marah"))
print("git the index of specific item example item 'mela':\n",namesOfGirls.index("mela"))
print ("check if the name mela is found in the namesOfGirls tuple : \n")
if "mela" in namesOfGirls:
    print("Yes,the name mela is found")
else:
    print("No,the name is not found")
number = (10,)*10
print("repeat the item in the list :\n",number)
# Iam applaying her the two example in this lession.
#example:1
x =(3,4,5,6)
x = x + (1,2,3)
print(" applay the + operator in tuple : ",x)
#example:2
thisList=[3,4,5,6,"A","B"]
thisTuple = tuple(thisList)
print("applaying tuple method",thisTuple)

