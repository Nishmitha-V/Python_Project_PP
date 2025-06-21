Words=eval(input("enter the list of words"))
long=0
for i in Words:
    if len(i)>long:
        long=len(i)
print(long)



