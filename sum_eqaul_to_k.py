def sum_equal_to_k(i,arr,sum):
    global n,k
    if i==n:
        if sum==k:
            print(arr)
        return
    
    arr.insert(len(arr),given_arr[i])
    sum+=given_arr[i]
    sum_equal_to_k(i+1,arr,sum)
    arr.remove(given_arr[i])
    sum-=given_arr[i]
    sum_equal_to_k(i+1,arr,sum)


given_arr=[1,2,1]
arr=[]
k=2
sum=0
n=len(given_arr)
sum_equal_to_k(0,arr,sum)