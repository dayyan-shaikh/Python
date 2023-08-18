l=["rose","lily","sunflower","dandelions"]
print(l)

#appending daisy in l
l.append("daisy")
print(l)

#inserting lily at index number 2
l.insert(2,"lily")
print(l)

#inserting sunflower at 0 index
l.insert(0,"sunflower")
print(l)

#deleting the second element
del l[1]
print(l)

#Deleting the first element
del l[0]
print(l)

#removing lily from l
l.remove("lily")
print(l)

#printong the index number of lily
index=l.index("lily")
print(index)

#copying l elements in m
m=l.copy()
print(m)

#clearing l variable and deleting m variable
l.clear()
del m 

print(l)
print(m)