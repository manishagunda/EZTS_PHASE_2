n=[]
m=int(input())
s=1
for i in range(m):
    b=[]
    for j in range(m):
        b.append(int(input()))
    n.append(b)
print("matrix\n")   
for i in range(m):
    for j in range(m):
        print(n[i][j],end=" ")
    print()

for i in range(m):
    for j in range(m):
        if(i==j and (n[i][j])%2!=0):
            s=s*n[i][j]

print("product=",s)
            

            


            
        
        
