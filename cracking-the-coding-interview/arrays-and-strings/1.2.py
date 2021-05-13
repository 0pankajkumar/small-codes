st1 = "tehelka"
st2 = "ethkael"

bank = dict()

for s in st1:
    if s in bank:
        bank[s] += 1
    else:
        bank[s] = 1

not_permutation = False

for s in st2:
    if s in bank:
        bank[s] -= 1
        if bank[s] < 0:
            not_permutation = True
            break
    else:
        not_permutation = True
        break


if not_permutation:
    print("Not a permutation")
else:
    print("Yes, a permutation")