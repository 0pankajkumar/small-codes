from collections import OrderedDict
bank = OrderedDict()


def fact(n):
    if n in bank:
        return bank[n]
    else:
        if len(bank) > 0:
            tem = list(bank.items())[-1]
            print(tem)
            s = tem[0]
            a = tem[1]
        else:
            s = 1
            a = 1
        for i in range(s, n):
            if i in bank:
                a *= bank[i]
                bank[i+1] = a
                print("Using cache")
            else:
                a *= i
                bank[i] = a
        return a


ans = fact(5)
print(bank)
ans = fact(6)
print(bank)
print(ans)
