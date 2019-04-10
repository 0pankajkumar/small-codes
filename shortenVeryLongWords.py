'''
Program to abbrevate very long words ( > 10 alphabets)using a notation
eg: "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n"

//Made for submission at codeforces
//by Pankaj Kumar
'''


n = int(input())

wordDrum = []

while(n > 0):
	word = input()
	if(len(word) > 10):
		outputString = word[0] + str(len(word)-2) + word[len(word)-1]
	else:
		outputString = word

	wordDrum.append(outputString)
	n -= 1

for i in wordDrum:
	print(i)
