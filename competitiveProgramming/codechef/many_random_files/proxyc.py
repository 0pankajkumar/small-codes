# cook your dish here
cases = int(input())

def percentage(strr, length):
    #calculating percentage
    p = 0
    for s in strr:
        if s == "P":
            p += 1
    
    per = (p / length)
    #print(per)
    return per

    
for cas in range(cases):
    length = int(input())
    strr = list(input())
    count = 0
    
    for i in range(length):
        # print(strr)
        # print(percentage(strr, length))
        if percentage(strr, length) >= 0.75:
            break
        if (i >= 2 and (i < length - 2)):
            if strr[i] == "A":
                #print(i)
                if (strr[i+1] == "P" or strr[i+2] == "P") and (strr[i-1] == "P" or strr[i-2] == "P"):
                    strr[i] = "P" #Marking Proxy
                    count += 1
                    #print("Still counting")

    if percentage(strr, length) >= 0.75:       
        print(count)
    else:
        print(-1)
