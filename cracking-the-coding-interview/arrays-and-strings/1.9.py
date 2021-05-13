def isSubstring(a, b):
    return b in a

def check_rotation(s1, s2):
    if len(s1) == len(s2) and len(s2) > 0:
        return isSubstring(s1+s1, s2)
    else:
        return False


s1 = "waterbottle"
s2 = "erbottlewat"

print(check_rotation(s1, s2))