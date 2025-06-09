def combination_sum(ind,target,arr):
    if target<0 or ind>=len(given_arr):
        return
    if target==0:
        print(arr)
        return
    
    arr.append(given_arr[ind])
    target-=given_arr[ind]
    combination_sum(ind,target,arr)
    arr.remove(given_arr[ind])
    target+=given_arr[ind]
    combination_sum(ind+1,target,arr)


given_arr=[2,3,6,7]
target=7
arr=[]
combination_sum(0,target,arr)