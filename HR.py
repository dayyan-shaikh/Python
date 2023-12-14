stud=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

num=[]
for i in range(len(stud)):
    num.append(stud[i][1])
num=list(set(num))
num.sort()
val=num[1]
name=[]
for i in range(len(stud)):
    if stud[i][1]==val:
        name.append(stud[i][0]) 
    
name.sort()
for i in name:
    print(i)
    