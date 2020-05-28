def AckFunc(m, n, s ="% s"): 
	print(s % ("A(% d, %d)" % (m, n))) 
	if m == 0: 
		return n + 1
	if n == 0: 
		return AckFunc(m - 1, 1, s) 
	n2 = AckFunc(m, n - 1, s % ("A(%d, %%s)" % (m - 1))) 
	return AckFunc(m - 1, n2, s) 

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

print(AckFunc(a, b))
