# My answer for Directi interview for internship
# Problem: To flatten the Array of Arrays
# This is a recusive approach that will take in any generic array


a = [1, 2, 3, 4, [11, 12, 13, 14], [5, 6, 7, 8, [15, 16, 17, 18]]]

arr = [1, 2, 3, [41, 42, 43], 5, [
    61, 62, [631, 632, 633, [6341, 6342, [63431, 63432]]]]]

final_var = []


def compressArray(a):
    for i in a:
        if(type(i) == int):
            final_var.append(i)
        else:
            compressArray(i)


compressArray(arr)
print(final_var)
