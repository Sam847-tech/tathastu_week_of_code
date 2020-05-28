size = int(input("\nEnter size of your list:"))
list=[]
for i in range(size):
    list.append(str(input("Enter element" + str(i+1) + " : ")))

flag=0
for i in range(size-2):
    for j in range(i+1,size-1):
        for k in range(i+2,size):
            sum = float(list[i])+float(list[j])+float(list[k])
            if 1<sum<2:
                flag=1
                print("The required triplet is: {}, {}, {}, with sum={}".format(list[i],list[j],list[k],sum))

if flag==0:
    print("No such triplet exists that is between 1 and 2")
