def print_spiral_order(mat):

    print("\nMatrix printed in spiral order: ")
    while mat:
        for x in mat.pop(0):
            print(x, end=" ")
        for v in mat:
            print(v.pop(), end=" ")
        if mat:
            for x in mat.pop()[::-1]:
                print(x, end=" ")
        for v in mat[::-1]:
            print(v.pop(0), end=" ")
            
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

mat = []

for i in range(row):
    a =[] 
    for j in range(col):
         a.append(int(input())) 
    mat.append(a)
print_spiral_order(mat)
