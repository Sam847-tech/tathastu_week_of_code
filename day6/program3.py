size = int(input("Enter size of array: "))
li = []
for i in range(size):
    li.append(int(input("Enter element number " + str(i + 1) + " : ")))

pos = 1
for i in li:
    if i==pos:
        pos+=1
        
print("Smallest positive number not in the list is:", pos)
