
choice=input("how many numbers after decimal point?")
quotient = []
divisor=7


for x in range(0,choice):
	remainder=22%7
	dividend=remainder*10
	while (temp<10):
		if (dividend/divisor)<temp:
			quotient=temp-1
			temp=temp+1
		temp+=1
	
	x+=1
	
print ("22/7 is ", quotient)