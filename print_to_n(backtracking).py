def print_to_n(i,n):
    if i<1:
        return
    else:
        print_to_n(i-1,n)
        print(i)


i,n=1,5
print_to_n(n,n)