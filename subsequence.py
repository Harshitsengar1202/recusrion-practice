def subseq(ind,arr):
    global n
    if ind>=n:
        print(arr)
        return
    else:
        arr.insert(len(arr),given_arr[ind])
        subseq(ind+1,arr)
        arr.remove(given_arr[ind])
        subseq(ind+1,arr)

arr=[]
given_arr=[3,1,2]
n=len(given_arr)
subseq(0,arr)