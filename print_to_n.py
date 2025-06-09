def print_to_n(i,n):
    if i>n:
        return
    else:
        print(i)
        print_to_n(i+1,n)

i,n=1,5
print_to_n(i,n)