# Fast Modulo exponetiation 


def moduloExpoRec(base,exp,mo):
	if exp==1:
		return base
	if exp%2==0:
		base1 = pow(moduloExpoRec(base,int(exp/2),mo),2)
		if base1 >= mo:
			return base1%mo
		else:
			return base1
	else:
		ans = (base * pow(moduloExpoRec(base,int((exp-1)/2),mo),2))
		if ans >= mo:
			return ans%mo
		else:
			return ans


mo = 1000000007
print(moduloExpoRec(4,13,497))