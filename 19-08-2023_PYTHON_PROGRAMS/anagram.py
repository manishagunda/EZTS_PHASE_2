a=input()
b=input()
a=a.lower()
b=b.lower()
c=[]
d=[]
for i in a:
    c.append(i)
for j in b:
    d.append(j)
c.sort()
d.sort()
if c==d:
    print("anagram")
else:
    print("not")