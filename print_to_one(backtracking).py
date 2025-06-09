def print_to_one(i,n):
    if i>n:
        return
    else:
        print_to_one(i+1,n)
        print(i)

i,n=1,5
print_to_one(i,n)
