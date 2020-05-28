lsize = int(input("Enter number of lists: "))
lelem = int(input("Enter number of elements in each list: "))
ls = []

for i in range(lsize):
    a =[] 
    for j in range(lelem):
         a.append(int(input("Enter element " + str(j+1) + " of list " + str(i+1) + " : "))) 
    ls.append(a)

ls2 = []
    
for i in ls:
    i.sort()
    ls2.extend(i)
    
ls2.sort()

print("\nSorted list is:", ls2)
