L=eval(input("enter a list of nos."))
O=0
E=0
N=0
for i in L:
    if i>0:
        if i%2!=0:
          O=O+i
        if i%2==0:
          E=E+i
    if i<0:
        N=N+i
print("Sum of even nos.",E)
print("Sum of odd nos.",O)
print("Sum of negative nos.",N)
