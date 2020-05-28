num = int(input("Enter the number upto which the Fibonacci series is to be found: "))
a = 0
b = 1
print("The Fibonacci series upto", num, "th number is as follows:")
for i in range(num-1):
    print(a, end=", ")
    c = a + b
    a = b
    b = c
print(a)
