# cook your dish here
cases = int(input())

def sumOfDigits(number):
    numberOfDigits = len(str(number))
    sum = 0
    while(number > 0):
        temp =  number % 10
        number = number // 10
        sum += temp
        numberOfDigits -= 1
    return sum
    
#print(sumOfDigits(123))
    
for cas in range(cases):
    #print("In test cases")
    n = int(input())
    nCounts = 1
    number = 19
    
    ans = number + 9 * (n - 1)
    
    # while(nCounts < n):
        
    #     #if(sumOfDigits(number) % 10 == 0):
    #     nCounts += 1
    #         #print(number)
    #     number += 9
            
    print(ans)