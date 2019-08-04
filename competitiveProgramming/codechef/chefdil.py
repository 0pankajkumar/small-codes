# cook your dish here
def toggle(ch):
    if ch == "1":
        return "0"
    if ch == "0":
        return "1"
    else:
        return ch


def calculate():
    nos = list(input())
    length = len(nos)
    # print(length)


    i = -1
    change_in_a_run = 0
    marked = 0

    while(True):
        i += 1
        # print(i)
        # print(nos)
        if(nos[i] == "1"):
            nos[i] = "X"
            marked += 1
            if i != 0:
                nos[i - 1] = toggle(nos[i - 1])
            if i != length - 1:
                nos[i + 1] = toggle(nos[i + 1])
            change_in_a_run += 1
        
        if (i == length - 1):
            i = -1
            if change_in_a_run == 0:
                break
            else:
                change_in_a_run = 0

    # print(marked)
    if marked == length:
        print("WIN")
    else:
        print("LOSE")
    
    
    
cases = int(input())

for cas in range(cases):
    calculate()