L=eval(input("enter a list of nos."))
Even=[]
Odd=[]
for i in L:
    if i%2==0:
        Even.append(i)
    if i%2!=0:
        Odd.append(i)
E=sorted(Even)
O=sorted(Odd)
print("largest even no.:",E[-1])
print("largest odd no.:",O[-1])
