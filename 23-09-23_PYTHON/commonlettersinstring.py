a=input()
b=input()
a=list(a)
b=list(b)
c=[]
co=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            co=1
            c.append(a[i])
if co==0:
    print("no")
else:
    print(set(c))
    

    
    
a=input()
b=input()
c=set()
co=0
for i in a:
    if i in b:
        co=1
        c.add(i)
if co==1:
    print(c)
else:
    print("no")
    
a=input()
b=input()
c=0
d={}
for i in a:
    d[i]=1
for i in b:
    if i in d:
        d[i]=d[i]+1
for i in d.keys():
    if d[i]>=
    
    