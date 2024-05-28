n=int(input("enter n"))
if n==1:
    print("monday")
elif n==2:
    print("tuesday")
elif n==3:
    print("wednesday")
elif n==4:
    print("thursday")
elif n==5:
    print("friday")
elif n==6:
    print("saturday")
else:
    print("sunday")
    
    
n=int(input("enter day num"))
switcher={
    1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"sunday"
}
print(switcher[n])
