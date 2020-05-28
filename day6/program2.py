import random

size = int(input("Enter size of list: "))

ls = []

for i in range(size):
    ls.append(random.randint(0,1))

print("Original list:", ls)

ls2 = []

for i in ls:
    if i==0:
      ls2.append(i)

for i in ls:
    if i==1:
      ls2.append(i)  

print("Sorted list:", ls2)
