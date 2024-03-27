# convert farenhiete to celcius
farenhiete=float(input("Enter the  tempreature in your place in farenhiete:"))
celcius=(farenhiete-32)/1.8
print(farenhiete," degrees farenhiete is equal to ", celcius,"degrees celcius",sep="@",end=" & ")
if celcius>=21.0 and celcius<=50.0:
    print("It is hot")
elif celcius>50:
    print("It is really hot")
elif celcius>=10.0 and celcius<=20.0:
    print("It is cold")
else :
    print("It is really cold")
