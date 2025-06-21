L= eval(input("enter a list "))
for i in L:
    s=L.count(i)
    if s%2!=0:
        print(i)
