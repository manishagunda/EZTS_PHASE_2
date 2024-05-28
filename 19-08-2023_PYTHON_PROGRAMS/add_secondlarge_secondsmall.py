a=list(map(int,input().split()))
b=[]
c=[]
for i in range(len(a)):
    if i%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
b.sort()
c.sort()
print(b)
print(c)
r=b[len(b)-2]+c[1]
print(r)

