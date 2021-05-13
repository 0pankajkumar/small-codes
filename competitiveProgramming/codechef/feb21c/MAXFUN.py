import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

test_cases = int(input())

for test in range(test_cases):
    n = int(input())

    arr = list(map(int, input().split()))

    ans = 0

    # for i in range(n-1):

    #     a = abs(arr[i] - arr[i+1])

    #     for j in range(i,n):
    #         b = abs(arr[i+1] - arr[j])
    #         c = abs(arr[j] - arr[i])
    #         ans = max(ans, a+b+c)

    maximum_to_right = [0]*n
    negative_to_right = [0]*n
    maximum_to_right[-1] = 0
    negative_to_right[-1] = 0
    grand_max = arr[-1]


    for i in range(n-1, -1, -1):
        local_max = max(abs(arr[i]), abs(grand_max))
        local_negative = arr[i] if arr[i] < 0 else None

        if local_negative and i+1 < n:
            if negative_to_right[i+1] > local_negative:
                negative_to_right[i] = local_negative
        else:
            negative_to_right[i] = local_max

        if local_max == abs(arr[i]):
            maximum_to_right[i] = arr[i]
            grand_max = arr[i]
        else:
            maximum_to_right[i] = grand_max


    for i in range(n-1):
        a = abs(arr[i] - arr[i+1])
        b = abs(arr[i+1] - maximum_to_right[i])
        c = abs(maximum_to_right[i] - arr[i])

        ans = max(ans, a+b+c)

        a = abs(arr[i] - arr[i+1])
        b = abs(arr[i+1] - negative_to_right[i])
        c = abs(negative_to_right[i] - arr[i])

        ans = max(ans, a+b+c)


    print(ans)
