def merge(arr,left,mid,right):
    left_arr=arr[left: mid+1]
    right_arr=arr[mid+1:right+1]
    
    left_ind=0
    right_ind=0
    ind=left
    
    while left_ind <len(left_arr) arrnd right_ind < len(right_arr):
        if left_arr[left_ind]<right_arr[right_ind]:
            arr[ind]=left_arr[left_ind]
            left_ind+=1
        else:
            arr[ind]=right_arr[right_ind]
            right_ind+=1
        ind+=1
        
    while right_ind<len(right_arr):
        arr[ind]=right_arr[right_ind]
        right_ind+=1
        ind+=1
        
    while left_ind<len(left_arr):
        arr[ind]=left_arr[left_ind]
        left_ind+=1
        ind+=1
    
def merge_sort(arr,left,right):
    if len(arr)==1:
        return
    mid=(left+right)//2
    merge_sort(arr,left,mid)
    merge_sort(arr,mid+1,right)
    
    merge(arr,left,mid,right)
    
    

arr=[56,32,78,43,67,89]
merge_sort(arr,0,len(arr)-1)
print(arr)