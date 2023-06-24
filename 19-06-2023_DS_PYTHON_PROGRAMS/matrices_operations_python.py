m=int(input("enter rows"))
n=int(input("enter columns"))
a=[]
for i in range(0,m):
    b=[]
    for j in range(0,n):
        c=int(input("enter element"))
        b.append(c)
    print(b)
    a.append(b)
print(a)
print("matrix form")
for i in range(m):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
print("diagonal elements")
for i in range(m):
    for j in range(n):
        if(i==j):
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("non diagonal elements")
for i in range(m):
    for j in range(n):
        if(i!=j):
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("upper diagonal elements")
for i in range(m):
    for j in range(n):
        if(i<j):
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("lower diagonal elements")
for i in range(m):
    for j in range(n):
        if(i>j):
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()

print("transpose matrix")
for i in range(m):
    for j in range(n):
        print(a[j][i],end=' ')
    print()
m1=int(input("enter rows"))
n1=int(input("enter columns"))
a1=[]
for i in range(0,m1):
    b1=[]
    for j in range(0,n1):
        c1=int(input("enter element"))
        b1.append(c1)
    print(b1)
    a1.append(b1)
print(a1)
print("matrix1")
for i in range(m):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
print("matrix2")
for i in range(m1):
    for j in range(n1):
        print(a1[i][j],end=' ')
    print()
print("addition")
for i in range(m):
    for j in range(n):
        print(a[i][j]+a1[i][j],end=' ')
    print()
print("multiplication")
for i in range(m):
    for j in range(n):
        print(a[i][j]*a1[i][j],end=' ')
    print()


    

