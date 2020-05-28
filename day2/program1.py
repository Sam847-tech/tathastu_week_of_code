num = int(input("Enter a number:"))

#odd/even
if(num % 2 == 0):
    print(num,"is an Even Number")
else:
    print(num,"is an Odd Number")

#prime
temp = num
a = 2
k = temp // 2
while k >= a:
    if temp % a == 0:
        print(num,"is not a Prime Number")
        break
    a += 1
    k = temp // a
if(k<a):
    print(num,"is a Prime Number")
    
#palindrome
ns = str(num)
l = len(ns)
for i in range(l // 2):
    if ns[i] == ns[l - 1 - i]:
        continue
    else:
        print(num,"is not a Palindrome Number")
        break
else:
    print(num,"is a Palindrome Number")
    
#armstrong
sum = 0  
temp = num  
while temp > 0:  
    digit = temp % 10
    sum += digit ** 3  
    temp //= 10  
if num == sum:  
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")
