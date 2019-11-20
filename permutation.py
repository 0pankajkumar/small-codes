import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')

def permute(s):
    # If length of s is 0 or 1
    # return s
    if len(s) == 0 or len(s) == 1:
        return [s]

    # else
    # remove 3 from s & place it at all possible places
    # pass s minus 3 to the magic function which will return
    #   whatever permutation is possible
    else:
        t = s[-1]
        pp = permute(s[:-1])
        permutations = []
        
        for p in pp:
            for i in range(len(s)):
                left = p[:i]
                right = p[i:]
                permutations.append(left + [t] + right)
        return permutations                

def driver():
    s = list("1234")
    result = permute(s)
    
    for r in result:
        print(''.join(r))

driver()