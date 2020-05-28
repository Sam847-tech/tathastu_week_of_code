size = int(input("Enter size of list: "))
ls = []

for i in range(size):
     ls.append(int(input("Enter element " + str(i+1) + " : "))) 

ls.sort()

print("\nLargest product of 3 nummbers in list is:", ls[-1]*ls[-2]*ls[-3])
