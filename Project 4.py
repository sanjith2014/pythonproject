list=[1,22,90,513,1027,0,34,54,43,12,90,11,13,10,67,111,333,88,3]
print(list,"is the list")
odd=[]
even=[]
for i in list:
    if i!=0:

     if i%2==0:
        even.append(i)

     else:
        odd.append(i)
    else:
        print(0,"from the list")
print("even numbers from list",even)
print("odd numbers from list",odd)
