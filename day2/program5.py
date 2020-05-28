n = int(input("Enter the value of N: "))

print("\n")
    
for i in range(n,0,-1):
    print((str(i) + "*") * (i-1) + str(i))
    
for i in range(2,n + 1):
    print((str(i) + "*") * (i-1) + str(i))
