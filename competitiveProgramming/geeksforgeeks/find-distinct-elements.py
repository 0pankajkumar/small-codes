#code

cases = int(input())

for cas in range(cases):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    setOfRow = [dict()] * n
    
    i = 0
    j = 0
    
    for a in arr:
        
        if i == n:
            i = 0
            j += 1
            break
        
        
        if a not in setOfRow[j]:
            setOfRow[j][a] = 1
        else:
            setOfRow[j][a] += 1
        
        
        # if a not in setOfRow:
        #     setOfRow[j].add(a)
        # else:
        #     setOfRow[j].remove(a)
        i += 1
        
    print(setOfRow)
    
    # masterSet = set()
    
    # for se in setOfRow:
        
    #     for s in se:
            
    #         masterSet.add(s)
            
    # print((masterSet))
    
        