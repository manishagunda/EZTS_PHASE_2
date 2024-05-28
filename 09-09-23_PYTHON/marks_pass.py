m1=int(input())
m2=int(input())
m3=int(input())
p=int(input())
if(m1>=p and m2>=p and m3>=p):
    print("pass")
else:
    print("nice try")
    
l=list(map(int,input().split()))
p=l[len(l)-1]
c=0
for i in range(len(l)):
    if(l[i]>=p):
        c+=1
if(c==len(l)):
    print("pass")
else:
    print("nice try")