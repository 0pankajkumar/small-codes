import sys, math  
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')  

# for t in range(int(input())):
jacketCost, sockCost, money = map(int, input().split())
money -= jacketCost
money = math.floor(money / sockCost)
if money % 2 == 0:
	print("Lucky Chef")
else:
	print("Unlucky Chef")	