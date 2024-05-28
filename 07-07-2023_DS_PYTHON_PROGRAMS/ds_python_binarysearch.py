a=[4,5,1,6,2,7,8,3,9,10]
a.sort()
print("sorted list",a)
e=6
l=0
h=9
f=0
while(l<=h):
    m=(l+h)//2
    if(e==a[m]):
        print("element found at location",m)
        f=1
        break
    elif(e<a[m]):
        h=m-1
    else:
        l=m+1
if(f==0):
    print("element not found")