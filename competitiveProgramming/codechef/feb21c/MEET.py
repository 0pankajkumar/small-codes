import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

import time
test_cases = int(input())
def parse_time(st):
    return time.strptime(st, "%I:%M %p")
for test in range(test_cases):
    meet = parse_time(input())
    n = int(input())
    ans = []
    for times in range(n):
        st = input()
        start = parse_time(st[:8])
        end = parse_time(st[9:])

        if start <= meet <= end:
            ans.append('1')
        else:
            ans.append('0')

    print(''.join(ans))
    # for a in ans:
    #     print(a, end="")
    # print()
