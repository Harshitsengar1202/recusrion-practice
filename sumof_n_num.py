def sumof_n(i):
    if i==0:
        return 0
    else:
        return i+sumof_n(i-1)

i=int(input("Enter the n:"))

print(sumof_n(i))