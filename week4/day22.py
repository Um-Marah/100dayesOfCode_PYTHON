# this program to applay about Python Dictionaries && day : 22
print("Empty Dictionary : ")
thisDic={}
print("thisDic =",thisDic)
print("creat and print Dictionary : ")
thisDic= {
    'name':'Fatimah ali',
    'age':26,
    'path':'Paython'
}
print("thisDic =",thisDic)
print("Accessing Items by Get the value of the key. ")
x=thisDic["path"]
print(x)
print("Accessing Items by get()method. ")
x=thisDic.get("name")
print(x)
print("Change Values")
thisDic["age"]=25
print("thisDic =",thisDic)
print(" Loop Through a Dictionary : print kays")
for x in thisDic:
    print(x)
print(" Loop Through a Dictionary : print Values")
for x in thisDic:
    print(thisDic[x])
print(" return values of a dictionary by values()method")
for x in thisDic.values():
    print(x)
print("use values()method without for loop ")
print(thisDic.values())
print("Loop through both keys and values, by using the items() function.")
for (x,y) in thisDic.items():
    print(x,y)
print("use items()method without for loop ")
print(thisDic.items())