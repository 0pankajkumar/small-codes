
def permute(s):
    # If length of s is 0 or 1
    # return s
    if len(s) == 0 or len(s) == 1:
        return s

    # else
    # remove 3 from s & place it at all possible places
    # pass s minus 3 to the magic function which will return
    #   whatever permutation is possible
    else:
        

def driver():
    s = "123"
    permute(s)

driver()