import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def check_validity(alpha, beta, funny_words_bank):
    alpha_mod = beta[0] + alpha[1:]
    beta_mod = alpha[0] + beta[1:]
    if alpha_mod in funny_words_bank:
        return False
    elif beta_mod in funny_words_bank:
        return False
    else:
        return True

test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    funny_words = list(input().split())
    funny_words_bank = set(funny_words)
    count = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if check_validity(funny_words[i], funny_words[j], funny_words_bank):
                count += 2

    print(count)