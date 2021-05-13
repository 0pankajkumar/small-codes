import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    weights = list(map(int, input().split()))
    lengths = list(map(int, input().split()))
    total_steps = 0
    steps = 0

    for i in range(n-1, -1, -1):

        if weights[i] < weights[i+1]:
            
            for j in range(i+1, n-1):

                if weights[j] < weights[i]:
                    steps += lengths[i]
