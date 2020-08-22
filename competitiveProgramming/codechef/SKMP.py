import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


for sss in range(int(input())):
    s = input()
    p = input()
    
    s_dict = dict()
    for a in s:
        if a not in s_dict:
            s_dict[a] = 1
        else:
            s_dict[a] += 1
            
    for a in p:
        s_dict[a] -= 1
        
    s_keys = list()
    for k,v in s_dict.items():
        s_keys.append(k)
        
    s_keys.sort()
    
    ans1 = []
    ans2 = []

    for a in s_keys:
        freq = s_dict[a]

        if a == p[0]:
            ans1.append(p)
            while freq > 0:
                ans1.append(a)
                ans2.append(a)
                freq -= 1
            ans2.append(p)
        else:
            while freq > 0:
                ans1.append(a)
                ans2.append(a)
                freq -= 1
    test1 = ''.join(ans1)
    test2 = ''.join(ans2)

    print(test1 if test1 < test2 else test2)