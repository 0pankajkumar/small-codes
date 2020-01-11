import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# for _ in range(int(input())):
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, -1)

s = set()
unknown = list()
for i in range(len(arr)):
    if arr[i] > 0:
        s.add(arr[i])
    elif arr[i] == 0:
        unknown.append(i)
# print(unknown)
k = 0
for j in range(n, 0, -1):
    if j not in s:
        arr[unknown[k]] = j
        k += 1

for i in range(1, n+1):
    print(arr[i], end=" ")
print()

# d = dict()
# for i in range(n):
#     d[i+1] = 0

# for i in range(n):
#     if arr[i] != 0:
#         d[arr[i]] = i+1

# print(d)

# flag = False
# for k, v in d.items():
#     if v == 0:
#         tk = k
#         tv = v


# unknown = list()
# for i in range(len(arr)):
#     if arr[i] == 0:
#         unknown.append(i)

# print(unknown)

# for i in range(1, len(unknown)):
#     if i+1 < len(unknown):
#         arr[unknown[i]] = unknown[i+1]
# arr[unknown[-1]] = unknown[1]

# for i in range(1, len(arr)):
#     print(arr[i], end=" ")
# print()
