size = int(input("Enter number of elements: "))
print("Enter elements in List")
list1 = []
for i in range(size):
    list1.append(input())

duplicateList = []
for x in list1:
    if x not in duplicateList:
        duplicateList.append(x)

print("List after removing duplicates:", duplicateList)
