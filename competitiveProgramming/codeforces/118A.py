
string = input().lower()
newString = ''
vowels = ['a','e','i','o','u']
for st in string:
	if st in vowels:
		continue
	else:
		newString += '.'
		newString += st

print(newString,end="")