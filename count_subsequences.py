def sum_equal_to_k(i,arr,sum):
    global n,k
    if i==n:
        if sum==k:
            return 1
        return 0
    
    sum+=given_arr[i]
    l=sum_equal_to_k(i+1,arr,sum)
    sum-=given_arr[i]
    r=sum_equal_to_k(i+1,arr,sum)
    return l+r

given_arr=[1,2,1]
arr=[]
k=2
sum=0
n=len(given_arr)
print(sum_equal_to_k(0,arr,sum))