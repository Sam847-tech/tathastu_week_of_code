def sortRot(ls,size):
    minE = min(ls)
    minI = ls.index(minE)
    
    if ls[0] == minE:
        print("List is not sorted and rotated")
        return
    
    if(ls[0] < ls[-1]):
        print("List is not sorted and rotated")
        flag=1
        return
    
    for i in range(1,size):
        if ls[i] == minE:
            continue
        elif ls[i] > ls[i-1]:
            continue
        else:
            print("List is not sorted and rotated")
            return
    	    
    print("List is sorted and rotated")
	
	

size = int(input("Enter size of array: "))
ls = []

for i in range(size):
    ls.append(int(input("Enter number " + str(i+1) + " : ")))
sortRot(ls, size)
