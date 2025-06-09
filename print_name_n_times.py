def print_name(i,n):
    if i>=n:
        return
    else:
        print("Harshit")
        print_name(i+1,n)

i,n=0,3
print_name(i,n)