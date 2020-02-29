# I tried this again
# Had this question 10 months before in Directi internship interview
# Refer flattenAnArrayOfArrays.py
# This solution here is a mess
# I have lost the flow of programming, it seems

arr = [1, 2, 3, [41, 42, 43], 5, [
    61, 62, [631, 632, 633, [6341, 6342, [63431, 63432]]]]]

crr = [50, 60, 70, 80]


def flat(brr, i, ans):
    # if i >= len(brr):
    # 	return
    # elif isinstance(brr[i], int):
    # 	return brr[i].extend(brr,i+1)

    if i >= len(brr):
        return []
    else:
        if isinstance(brr[i], int):
            if i == len(brr)-1:
                return [brr[i]]
            else:
                temp = [brr[i]]
                temp.extend(flat(brr, i+1, ans))
                return temp
        else:
            temp = []
            temp.extend(flat(brr, i, ans))
            return temp


ans = []
print(flat(arr, 0, ans))
