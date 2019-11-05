# Classsical approach: find brute force, optimise that
# cook your dish here

cases = int(input())

for cas in range(cases):

    n = int(input())
    
    strung = input()

    ccount = 0
    count = 0

    # Brute force approach
    # for i in range(n):
    #     if strung[i] == '1':
    #         for j in range(i+1):
    #             if strung[j] == '1':
    #                 count += 1

    for i in range(n):
        if strung[i] == '1':
            ccount += 1
            count += ccount


    print(count)












