def swap(arr,i,n):
    arr[i],arr[n]=arr[n],arr[i]
    

def reverse(arr,i,n):
    if i>=n/2:
        return
    else:
        swap(arr,i,n-i-1)
        reverse(arr,i+1,n)


n=int(input("Enter the size of array:"))
print("Enter the elements:")
arr=[0]*n
for i in range(n):
    arr[i]=int(input())
reverse(arr,0,n)
print(arr)