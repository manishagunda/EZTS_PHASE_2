num = int(input())
temp=num
count = 0
while num != 0:
    num //= 10
    count += 1
print("Number of digits:",(count))
if(temp%count==0):
    print("divisible")
else:
    print("not divisible")