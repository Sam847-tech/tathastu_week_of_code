maxLim = 100005
fibonacci = set() 

def createFib(): 

	prev , curr = 0, 1

	fibonacci.add(prev) 
	fibonacci.add(curr) 

	while (curr <= maxLim): 
		temp = curr + prev 
		if temp <= maxLim: 
			fibonacci.add(temp) 
		prev = curr
		curr = temp


size = int(input("Enter size of array: "))
ls = []

for i in range(size):
    ls.append(int(input("Enter number " + str(i+1) + " : ")))

createFib()

sum = 0
for i in range(size): 
	if (ls[i] in fibonacci):
		sum += ls[i] 
		
if (sum in fibonacci): 
	print("\nSum", sum, "is a fibonacci number")
else:
    print("\nSum", sum, "is not a fibonacci number")
