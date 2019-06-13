n= int(input())

def roundUp(numToRound, multiple):
    if(multiple == 0):
        return numToRound

    remainder = numToRound % multiple

    if(remainder == 0):
        return numToRound
    
    ans = (numToRound - remainder - multiple)
    if ans == 0:
        return ans + multiple
    else:
        return ans

    # if(remainder < round(multiple / 2)):
    #     return (numToRound - remainder)
    # else:
    #     return numToRound + multiple - remainder




for i in range(0,n):
    # True means Ari
    # False means Rich in chance
    chance = False
    s = input().split()
    
    N = int(s[0])
    M = int(s[1])

    while(N > 0 and M > 0):
        chance = not chance
        if(N>M):
            N -= roundUp(N,M)
        else:
            M -= roundUp(M,N)
        #print(f"{N} {M}")
    
    print("Ari") if chance == True else print("Rich")
    