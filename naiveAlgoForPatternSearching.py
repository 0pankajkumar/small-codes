
txt = "TTTTTTTTTTB"
pat = "TTTT"

flag = False

txtLoopCount = 0
patLoopCount = 0

for i in  range(0, len(txt)):
    txtLoopCount += 1
    p = i
    # print(f"Outer loop {i}")
    for j in range(0, len(pat)):
        patLoopCount += 1
        if txt[p-1] == pat[j]:
            # print(p)
            p += 1
            if (j+1) == len(pat):
                flag = True
        else:
            break

    if flag == True:
        print(f"Patten found at {i}")
        flag = False

print(f"m = {txtLoopCount}")
print(f"n = {patLoopCount}")
