cases = int(input())

for cas in range(cases):
    num = input()
    if int(num)%10==0:
        print(num)
        continue
    if len(num) > 2:
        start = num[:-2]
        if num[-2] == '0':
            start += '0'
        end = int(num[-2] + num[-1])
    else:
        start = ''
        end = int(num)
    rem = end%10
    intens = end - rem
    ans = None
    if end-intens > 5:
        ans = intens+10
    else:
        ans = intens
    
    if len(str(ans)) > 2:
        buff = ''
        for i in range(len(start)):
            buff += '0'
        print(str(ans) + buff)
    else:
        print(start+str(ans))
    