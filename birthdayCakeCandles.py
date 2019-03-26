
# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count = 1
    max = ar[0]
    for i in range(0,ar_count):
        if ar[i+1] > max:
            max == ar[i+1]
            if count > 1:
                count = 1
        elif ar[i+1] == max:
            count += 1
    
    return count
ar = [3,1,2,3]
ar_count = 4
print birthdayCakeCandles(ar)