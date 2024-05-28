a=[4,2,3,1,6,5]
n=len(a)
for i in range(n-1):
    min=a[i]
    pos=i
    for j in range(i+1,n):
        if(min>a[j]):
            min=a[j]
            pos=j
        else:
            min=min
    a[pos]=a[i]
    a[i]=min
print(a)