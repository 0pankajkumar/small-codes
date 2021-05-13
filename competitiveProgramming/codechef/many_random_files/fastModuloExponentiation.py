# Fast Modulo exponetiation 

def modularExpoNaive(base, exp, mo):
	ans = 1
	while(exp):
		if exp%2==1:
			ans = (ans*base)%mo
		base = (base*base)%mo
		exp/=2
	return ans

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

def moduloExpoLoop(base,exp,mo):
	res = 1
	while exp > 0:
		if exp%2==1:
			res = (res*base)%mo 
		base=(base*base)%mo
		exp = int(exp / 2)
	return res%mo

mo = 1000000007
print(moduloExpoRec(4,13,497))