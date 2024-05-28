n=list(map(int,input().split(",")))
a=int(input("enter sum"))
for i in range(len(n)): #time complexity is O(n)
  for j in range(i+1,len(n)):#time complexity is O(n); total is O(n^2)
    if(a==n[i]+n[j]):
        print("yes")
        print(n[i],n[j])
        
        
n=list(map(int,input().split(",")))
a=int(input("enter sum"))
n.sort() #merge sort time complexity is O(n logn)
i=0
j=len(n)-1
while(i<j): #time complexity is O(n)
    if n[i]+n[j]==a:
        print(n[i],n[j])
        i+=1
        j-=1
    elif n[i]+n[j]>a:
        j=j-1
    else:
        i=i+1


n=list(map(int,input().split(",")))
a=int(input("enter sum"))        
d={}
for i in n:
    d[i]=1
for i in n:
    if a-i in d:
        print("true",i,a-i)
        c=1
        break
if c==0:
    print("no")

    