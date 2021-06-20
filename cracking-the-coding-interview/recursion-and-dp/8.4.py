

def subsets(arr, supra):
    if len(arr) <= 0:
        return
    else:
        supra.add(tuple(arr))
    
    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i+1:]
        # print("->", arr, i, end="<-")
        subsets(new_arr, supra)
        # print(new_arr)



s = [1, 2, 3]
supra = set()
subsets(s, supra)

for sup in supra:
    print(sup)
