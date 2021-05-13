# cook your dish here
import math

def dictIt(strin):
    d = dict()

    for s in strin:
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1

    return d


def compareDicts(s1, s2):

    doinfGood = False

    for key1, value1 in s1.items():
        if key1 in s2:
            if s2[key1] == s1[key1]:
                doinfGood = True
        else:
            return False

    return doinfGood




cases = int(input())

for cas in range(cases):
    
    strung = input()
    
    if(len(strung) % 2 != 0):
        
        s1 = strung[:math.floor(len(strung) / 2)]
        s2 = strung[math.floor(len(strung) / 2) + 1 :]
        
        # s1 = dictIt(s1)
        # s2 = dictIt(s2)

        # res = compareDicts(s1, s2)

        s1 = list(s1)
        s2 = list(s2)

        s1.sort()
        s2.sort()

        s1 = ''.join(s1)
        s2 = ''.join(s2)

        print("YES" if s1 == s2 else "NO")
        
    else:
        # print(len(strung) / 2)
        # print(((len(strung) / 2) + 1))
        s1 = strung[ : int((len(strung)) / 2)]
        s2 = strung[int((len(strung) / 2)) : ]

        # s1 = dictIt(s1)
        # s2 = dictIt(s2)

        # res = compareDicts(s1, s2)

        # print("YES" if res else "NO")

        s1 = list(s1)
        s2 = list(s2)

        s1.sort()
        s2.sort()

        s1 = ''.join(s1)
        s2 = ''.join(s2)

        print("YES" if s1 == s2 else "NO")
        
        