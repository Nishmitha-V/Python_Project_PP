L=eval(input("enter a list of nos."))
Even=[]
Odd=[]
for i in L:
    if i%2==0:
        Even.append(i)
    if i%2!=0:
        Odd.append(i)

print("Even",Even)
print("Odd",Odd)