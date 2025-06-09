def print_to_one(i,n):
    if n<i:
        return
    else:
        print(n)
        print_to_one(i,n-1)

i,n=1,5
print_to_one(i,n)