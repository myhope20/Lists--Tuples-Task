#List
a=["Apple","Banana","Cherry"]
print(a[2])
print(a[-2])

#Insert and Remove

a=["a","b","c","d"]
a.insert(2,"e")
a.remove("b")
print(a)

#POP
a=["a","b","c","d"]
a.pop()
a.pop(2)

print(a)

#Sort
a=["a","b","c","d"]
a.sort(reverse=True)
a.reverse()
print(a)

#List Comprehesion

a=[x*2 for x in range(1,6)]
print(a)


#extend
a=["a","b","c","d"]
a.extend(["e","f","h"])
print(a)

#Copy
a=["a","b","c","d"]
b=a.copy()
print(b)

#Clear
a=["a","b","c","d"]
a.clear()
print(a)

#Membership Opeartor
a=["a","b","c","d"]
print("e" in a)

#Updating List
a=["a","b","c","d"]
a[1]="h"
print(a)

#Deleting a List
a=["a","b","c","d"]
del a[2]
print(a)

#Tuple
a=("a","b","c","d","a","a")
#indexing
print (a[2])
#Negative Indexing
print(a[-3])
#Slicing
print(a[1::3])
print(a[:4])
#Count
print(a.count("a"))
#Index
print(a.index("a"))

#Packing
'''a=("Mohan",31,"Python")
print(a)'''
#Unpacking
b=("Mohan",31,"Python")
name,age,course=b
print(b)


#Membership Opeartor
a=("Mohan",31,"Python")
print(31 in a)
print(len(a))
print(a)

#Nested Tuple
a=(("Mohan","raj"),("Python","Java"))
print(a)
print(a[0])
#Conversting tuple to list
a=list(a)
a.append("C++")
a=tuple(a)
print(a)

