def subseq(ind,arr,sum):
    global n
    if ind>=n:
        print(arr,":",sum)
        return
    else:
        arr.insert(len(arr),given_arr[ind])
        sum+=given_arr[ind]
        subseq(ind+1,arr,sum)
        arr.remove(given_arr[ind])
        sum-=given_arr[ind]
        subseq(ind+1,arr,sum)

arr=[]
sum=0
given_arr=[3,1,2]
n=len(given_arr)
subseq(0,arr,sum)