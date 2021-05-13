st = "Tact Coa"

st = st.strip().replace(" ", "").lower()

# Lets count
bank = dict()
for s in st:
    if s in bank:
        bank[s] += 1
    else:
        bank[s] = 1

# check
center_already_found = False
pallindrome = True
for k,v in bank.items():
    if v % 2 != 0:
        if v == 1:
            if not center_already_found:
                center_already_found = True
            else:
                pallindrome = False
                break
        else:
            pallindrome = False
            break

if pallindrome:
    print("Pallindrome")
else:
    print("No not a pallindrome")