print("Enter the numbers seperated by a space")
k=input()
l=k.split()
j=[]
for i in range(0,len(l)):
    if(not int(l[i])<0):
        j.append(int(l[i]))
del l
print(j)


