def PermutationStep(num):
    if sorted(list(str(num)), reverse=True) == list(str(num)):
        return "It is already the greatest number"
    ls = list(str(num))
    n = 0
    inx = 0
    for ind, i in enumerate(ls[::-1]):
        if int(i) < n:
            n = int(i)
            inx = -(ind + 1)
            break
        n = int(i)
    ls[inx], ls[inx + 1] = ls[inx + 1], ls[inx]

    nl = ls[inx::-1][::-1]
    ln = sorted(ls[inx+1:])
    st = ''.join(nl) + ''.join(ln)
    return "The next greater number is " + st

num = input("Enter a number: ")
print(PermutationStep(num))
