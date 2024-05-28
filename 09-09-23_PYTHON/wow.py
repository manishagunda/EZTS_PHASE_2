a=input()
s=list(a)
c=0
for i in range(len(s)):
    if(s[i-1]==s[i]):
        c+=1
if(c==0):
    print("wow")
else:
    print(c)
