#Estimating validity of a credit/debit card using Luhn's algorithm

n = []  #Used for taking input in a list
sonu = []   #Odd places stored in this list
monu = 0    #Even places are kept adding on this int variable
sonu2 = 0   #lastly, adding the contents of sonu[] after adding double digits after multiplication
f = 1       #This is a variable to determine even or odd
for i in range(0,16):   #loop taking input
	n.append(input())
	
for i in range(0,16):   #loop for sorting even odd places & operating on them
    if f%2 == 0:        #Operation on even places
		monu += n[i]
		n[i] = 0
    
    else:               #Operation on odd places
		
		n[i] *= 2
		if n[i] > 9:
			temp = n[i] % 10
			n[i] = n[i] - temp
			n[i] = n[i] / 10
			n[i] = n[i] + temp
            
    f+=1
			
for i in range(0,16):   #Adding all even places
    sonu2 += n[i]
	
if (sonu2 + monu)%10 == 0:      #printing validity of a credit/debit card
    print "\n\n Its a valid Card"
else:
	print "\n\nError: An invalid card entered.\n Aborting"