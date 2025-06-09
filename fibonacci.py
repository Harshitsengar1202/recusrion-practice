def fibbo(n):
    if n<=1:
        return n
    else:
        second= fibbo(n-1)
        last=fibbo(n-2)
        return second+last
    

n=int(input("Enter the n:"))
print("Fibbonacci Series......")
for i in range(n+1):
    print(fibbo(i))