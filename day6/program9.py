size = int(input("Enter size of array: "))
ls = []
for i in range(size):
    ls.append(int(input("Enter number "+ str(i+1) + " : "))) 
k = int(input("Enter Kth element: "))  

ls.sort()
print("Kth smallest element in array: ",ls[k-1])
