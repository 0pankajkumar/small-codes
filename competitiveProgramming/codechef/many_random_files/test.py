


def putZerosOnRepeat(a):
    b = list(str(a))
    temp = "X"
    for i in range(len(b)):
        if b[i] == temp:
            b[i] = "0"
        else:
            temp = b[i]
    c = ''.join(b)
    print(int(c))

putZerosOnRepeat(66667122336778)



