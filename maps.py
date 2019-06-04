import collections

dict1 = {'day1':'Mon', 'day2':'Tue'}
dict2 = {'day1':'Jan', 'day2': 'feb', 'day3': 'mar'}
# dict3 = {'day1':'Jan', 'day2': 'feb'}

print(dict1)
print(dict2)

res = collections.ChainMap(dict2, dict1)

print(list(res.keys()))
print()

for keyy, vall in res.items():
	print(f"{keyy} = {vall}")
