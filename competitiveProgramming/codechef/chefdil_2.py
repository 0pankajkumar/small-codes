# A recursive approach
def toggle(ch):
    if ch == "1":
        return "0"
    if ch == "0":
        return "1"
    else:
        return ch

def recur(nos,i):
	length = len(nos)
	if(nos[i] == "1"):
		nos[i] = "X"
		if i != 0:
			nos[i - 1] = toggle(nos[i - 1])
			if nos[i - 1] == "1":
				recur(nos, i - 1)
		if i != length - 1:
			nos[i + 1] = toggle(nos[i + 1])
			if nos[i - 1] == "1":
				recur(nos, i + 1)


def calculate():
    nos = list(input())
    length = len(nos)
    # print(length)


 
    change_in_a_run = 0
    marked = 0

    for i in range(length):
    	recur(nos,i)

    if "0" in nos or "1" in nos:
    	print("LOSE")
    else:
    	print("WIN")
    	


    
    
    
cases = int(input())

for cas in range(cases):
    calculate()