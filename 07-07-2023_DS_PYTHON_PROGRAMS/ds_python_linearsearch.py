arr=[5,3,2,6,4,0,23]
key=3
found=False
for i in range(len(arr)):
    if arr[i]==key:
        print("element found",i)
        found=True
        break
if found==False:
    print("element not found")